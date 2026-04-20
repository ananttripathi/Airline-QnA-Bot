import os
import gradio as gr
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

PDF_PATH = "Dataset - Flykite Airlines_ HRP.pdf"
FAISS_INDEX_PATH = "faiss_index"
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

SYSTEM_PROMPT = """You are an expert HR assistant for Flykite Airlines. \
Answer employee questions clearly and accurately using only the HR policy \
document context provided below.

Guidelines:
- Be concise but thorough
- Use bullet points for lists or multi-part answers
- Always cite the relevant policy area (e.g. "Per the Leave Policy...")
- If the answer is not in the context, say: \
"I couldn't find that in the Flykite HR handbook. Please contact HR directly."

Context from HR Handbook:
{context}"""


def build_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
    if os.path.exists(FAISS_INDEX_PATH):
        return FAISS.load_local(
            FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True
        )
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    chunks = splitter.split_documents(docs)
    vs = FAISS.from_documents(chunks, embeddings)
    vs.save_local(FAISS_INDEX_PATH)
    return vs


print("Loading HR handbook and building index...")
vectorstore = build_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY,
    temperature=0.2,
    max_tokens=1024,
)
print("Ready.")


def respond(message: str, history: list) -> str:
    docs = retriever.invoke(message)
    context = "\n\n".join(doc.page_content for doc in docs)

    messages = [SystemMessage(content=SYSTEM_PROMPT.format(context=context))]
    for msg in history:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            messages.append(AIMessage(content=msg["content"]))
    messages.append(HumanMessage(content=message))

    answer = llm.invoke(messages).content

    pages = sorted(set(doc.metadata.get("page", 0) + 1 for doc in docs))
    if pages:
        answer += f"\n\n*📄 Referenced pages: {', '.join(str(p) for p in pages)}*"

    return answer


demo = gr.ChatInterface(
    fn=respond,
    type="messages",
    title="✈️ Flykite Airlines HR Policy Assistant",
    description=(
        "Instant answers from the official Flykite Airlines HR handbook.\n\n"
        "**Ask about:** Leave policies · Benefits · Code of conduct · Disciplinary procedures · Compliance"
    ),
    examples=[
        "What is the annual leave entitlement for employees?",
        "How many sick days are employees entitled to per year?",
        "What is the code of conduct for cabin crew?",
        "What are the disciplinary procedures for policy violations?",
        "What benefits are available to full-time employees?",
        "What is the grievance redressal process?",
    ],
    theme=gr.themes.Soft(primary_hue="blue", secondary_hue="indigo", neutral_hue="slate"),
    fill_height=True,
)

if __name__ == "__main__":
    demo.launch()
