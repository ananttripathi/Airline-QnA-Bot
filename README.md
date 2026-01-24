# Flykite Airlines HR Policy Assistant - RAG-Powered Chatbot

## Business Context

Modern organizations operate in an environment where internal policies have grown increasingly complex, covering areas such as leaves, reimbursements, travel, hybrid work norms, performance management, compliance, and more. These policies are commonly documented in static, lengthy HR handbooks or PDFs, which employees often find difficult to understand, search, or apply in their daily work scenarios.

### Current Challenges

As a result of complex policy documentation:

- **HR teams** are burdened with repetitive queries about standard policies, diverting their focus from strategic initiatives
- **Employees** struggle with confusion or non-compliance, as the dense and static format of policy documents obscures the necessary guidance
- **Both sides** suffer from reduced productivity:
  - HR spends excessive time addressing routine questions
  - Employees experience delays in obtaining the information they need to perform efficiently

Addressing these challenges requires modern HR systems that centralize policy information, simplify access, and deliver clear, actionable insights. By leveraging technology to streamline policy communication and automate routine queries, organizations can enhance clarity, boost compliance, and ultimately improve overall operational efficiency.

## Objective

The goal is to develop a prototype that demonstrates how Natural Language Processing (NLP), powered by Retrieval-Augmented Generation (RAG), can help employees efficiently query company HR policies and receive accurate, context-aware, and easily understandable answers.

### Specific System Goals

The system aims to:

1. **Answer employee questions** by retrieving relevant content from official HR handbooks and policy documents
2. **Handle ambiguous queries** and follow-up questions by clarifying intent and distinguishing between similar policy categories (e.g., sick leave versus casual leave)
3. **Personalize responses** based on role, location, or department, acknowledging that policies may differ (e.g., field staff versus HQ)
4. **Increase trust and compliance** by citing sources (document name, section, and clause) for each response

## Sample Questions to Answer

1. What are the effects on the benefits I receive if my probation is extended?
2. There has been a demise in my family last night, and I need to attend the last rites. How should I inform the office, and will I be granted leave?
3. What should I do if I notice suspected harassment with my female colleague?

## Data Description

The employee handbook is an internal reference published by **Flykite Airlines** that outlines a wide range of workplace policies, guidelines, and procedures for staff. The handbook is provided in **PDF format** and serves as a comprehensive resource for employees across different roles within the airline.

## Evaluation Rubrics

### Interim Report (Total: 40 Points)

| Section | Description | Points |
|---------|-------------|--------|
| **Question Answering using LLM** | - Load the large language model<br>- Create a function to define the model parameters and generate a response<br>- Apply the response generation function to get answers to the questions provided in the problem statement<br>- Evaluate the responses for groundedness and relevance<br>- Provide comments/observations for the answers received | 10 |
| **Question Answering using LLM and Prompt Engineering** | - Refine prompts or input formatting to improve the quality of answers<br>- Apply the response generation function to get answers to the questions provided in the problem statement<br>- Evaluate the responses for groundedness and relevance<br>- Provide comments/observations for the answers received | 10 |
| **Data Preparation for RAG** | - Load the data file provided<br>- Split the data using a text splitter with the necessary attributes<br>- Load the embedding model<br>- Load the vector database<br>- Define the retriever with an appropriate search method and k value<br>- Test the retriever by fetching relevant chunks of data as per the provided questions | 14 |
| **Business Report Quality** | - Adhere to the business report checklist | 6 |

### Final Report (Total: 60 Points)

| Section | Description | Points |
|---------|-------------|--------|
| **Question Answering using LLM** | - Load the large language model<br>- Create a function to define the model parameters and generate a response<br>- Apply the response generation function to get answers to the questions provided in the problem statement<br>- Evaluate the responses for groundedness and relevance<br>- Provide comments/observations for the answers received | 5 |
| **Question Answering using LLM and Prompt Engineering** | - Refine prompts or input formatting to improve the quality of answers<br>- Apply the response generation function to get answers to the questions provided in the problem statement<br>- Evaluate the responses for groundedness and relevance<br>- Provide comments/observations for the answers received | 3 |
| **Data Preparation for RAG** | - Load the data file provided<br>- Split the data using a text splitter with the necessary attributes<br>- Load the embedding model<br>- Load the vector database<br>- Define the retriever with an appropriate search method and k value<br>- Test the retriever by fetching relevant chunks of data as per the provided questions | 7 |
| **Question Answering using RAG** | - Apply the response generation function to get answers to the questions provided in the problem statement<br>- Evaluate the responses for groundedness and relevance<br>- Provide comments/observations for the answers received | 10 |
| **Question Answering using RAG Fine Tuning** | - Tune the hyperparameters of the RAG system (try 5 combinations at least)<br>- Apply the response generation function to get answers to the provided questions using each combination above<br>- Evaluate the responses for groundedness and relevance<br>- Provide comments/observations for the answers received | 25 |
| **Actionable Insights and Recommendations** | - Compare and comment on the performance of all the methods tried so far<br>- Key takeaways for the business | 4 |
| **Business Report Quality** | - Adhere to the business report checklist | 6 |

---

## Project Structure
```
flykite-hr-assistant/
├── README.md
├── requirements.txt
├── data/
│   └── employee_handbook.pdf
├── notebooks/
│   ├── interim_report.ipynb
│   └── final_report.ipynb
├── src/
│   ├── llm_setup.py
│   ├── data_preparation.py
│   ├── rag_pipeline.py
│   ├── evaluator.py
│   └── utils.py
├── embeddings/
│   └── vector_store/
└── docs/
    └── business_report.md
```

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/flykite-hr-assistant.git
cd flykite-hr-assistant

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

## Usage

### Basic Query Example
```python
from src.rag_pipeline import HRPolicyAssistant

# Initialize the assistant
assistant = HRPolicyAssistant()

# Ask a question
question = "What are the effects on benefits if probation is extended?"
response = assistant.query(question)

print(response['answer'])
print(f"Source: {response['source']}")
```

### RAG Pipeline Setup
```python
from src.data_preparation import prepare_documents
from src.rag_pipeline import build_rag_pipeline

# Prepare documents
chunks = prepare_documents('data/employee_handbook.pdf')

# Build RAG pipeline
rag_chain = build_rag_pipeline(chunks)

# Query the system
result = rag_chain.invoke("How do I apply for bereavement leave?")
```

## Technologies Used

- **Python 3.8+**
- **LangChain** - RAG framework
- **OpenAI GPT / Anthropic Claude** - Large Language Models
- **Hugging Face Transformers** - Embedding models
- **FAISS / ChromaDB** - Vector databases
- **PyPDF2 / PDFPlumber** - PDF processing
- **Pandas & NumPy** - Data manipulation

## Key Features

- 📚 **Document Processing**: Efficiently processes HR policy PDFs
- 🔍 **Semantic Search**: Retrieves relevant policy sections using vector embeddings
- 💬 **Context-Aware Responses**: Generates accurate answers grounded in source documents
- 📝 **Source Attribution**: Cites specific sections and clauses from policy documents
- ⚙️ **Hyperparameter Tuning**: Optimizable RAG pipeline for best performance
- 📊 **Evaluation Metrics**: Groundedness and relevance scoring

## RAG System Components

### 1. Document Loading & Chunking
- Load PDF employee handbook
- Split into manageable chunks using appropriate text splitters
- Preserve context and section boundaries

### 2. Embedding & Vector Storage
- Generate embeddings using state-of-the-art models
- Store in vector database (FAISS/ChromaDB)
- Enable fast similarity search

### 3. Retrieval
- Implement semantic search with configurable k value
- Support multiple search methods (similarity, MMR, etc.)
- Return relevant document chunks

### 4. Generation
- Use LLM to generate responses based on retrieved context
- Apply prompt engineering for better outputs
- Include source citations

## Evaluation Metrics

- **Groundedness**: How well the answer is supported by retrieved documents
- **Relevance**: How well the answer addresses the user's question
- **Source Attribution**: Accuracy of citations and references

## Hyperparameter Tuning

The RAG system supports tuning of:
- Chunk size and overlap
- Number of retrieved documents (k)
- Embedding model selection
- Retrieval algorithm (similarity, MMR, etc.)
- LLM temperature and parameters

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please contact: [your-email@example.com]

## Acknowledgments

- Flykite Airlines for providing the employee handbook dataset
- LangChain community for RAG framework
- OpenAI/Anthropic for LLM APIs
```

---

# In Code Format (Raw Text)
```
# Flykite Airlines HR Policy Assistant - RAG-Powered Chatbot

## Business Context

Modern organizations operate in an environment where internal policies have grown increasingly complex, covering areas such as leaves, reimbursements, travel, hybrid work norms, performance management, compliance, and more. These policies are commonly documented in static, lengthy HR handbooks or PDFs, which employees often find difficult to understand, search, or apply in their daily work scenarios.

### Current Challenges

As a result of complex policy documentation:

- **HR teams** are burdened with repetitive queries about standard policies, diverting their focus from strategic initiatives
- **Employees** struggle with confusion or non-compliance, as the dense and static format of policy documents obscures the necessary guidance
- **Both sides** suffer from reduced productivity:
  - HR spends excessive time addressing routine questions
  - Employees experience delays in obtaining the information they need to perform efficiently

Addressing these challenges requires modern HR systems that centralize policy information, simplify access, and deliver clear, actionable insights. By leveraging technology to streamline policy communication and automate routine queries, organizations can enhance clarity, boost compliance, and ultimately improve overall operational efficiency.

## Objective

The goal is to develop a prototype that demonstrates how Natural Language Processing (NLP), powered by Retrieval-Augmented Generation (RAG), can help employees efficiently query company HR policies and receive accurate, context-aware, and easily understandable answers.

### Specific System Goals

The system aims to:

1. **Answer employee questions** by retrieving relevant content from official HR handbooks and policy documents
2. **Handle ambiguous queries** and follow-up questions by clarifying intent and distinguishing between similar policy categories (e.g., sick leave versus casual leave)
3. **Personalize responses** based on role, location, or department, acknowledging that policies may differ (e.g., field staff versus HQ)
4. **Increase trust and compliance** by citing sources (document name, section, and clause) for each response

## Sample Questions to Answer

1. What are the effects on the benefits I receive if my probation is extended?
2. There has been a demise in my family last night, and I need to attend the last rites. How should I inform the office, and will I be granted leave?
3. What should I do if I notice suspected harassment with my female colleague?

## Data Description

The employee handbook is an internal reference published by **Flykite Airlines** that outlines a wide range of workplace policies, guidelines, and procedures for staff. The handbook is provided in **PDF format** and serves as a comprehensive resource for employees across different roles within the airline.

## Evaluation Rubrics

### Interim Report (Total: 40 Points)

| Section | Description | Points |
|---------|-------------|--------|
| **Question Answering using LLM** | - Load the large language model<br>- Create a function to define the model parameters and generate a response<br>- Apply the response generation function to get answers to the questions provided in the problem statement<br>- Evaluate the responses for groundedness and relevance<br>- Provide comments/observations for the answers received | 10 |
| **Question Answering using LLM and Prompt Engineering** | - Refine prompts or input formatting to improve the quality of answers<br>- Apply the response generation function to get answers to the questions provided in the problem statement<br>- Evaluate the responses for groundedness and relevance<br>- Provide comments/observations for the answers received | 10 |
| **Data Preparation for RAG** | - Load the data file provided<br>- Split the data using a text splitter with the necessary attributes<br>- Load the embedding model<br>- Load the vector database<br>- Define the retriever with an appropriate search method and k value<br>- Test the retriever by fetching relevant chunks of data as per the provided questions | 14 |
| **Business Report Quality** | - Adhere to the business report checklist | 6 |

### Final Report (Total: 60 Points)

| Section | Description | Points |
|---------|-------------|--------|
| **Question Answering using LLM** | - Load the large language model<br>- Create a function to define the model parameters and generate a response<br>- Apply the response generation function to get answers to the questions provided in the problem statement<br>- Evaluate the responses for groundedness and relevance<br>- Provide comments/observations for the answers received | 5 |
| **Question Answering using LLM and Prompt Engineering** | - Refine prompts or input formatting to improve the quality of answers<br>- Apply the response generation function to get answers to the questions provided in the problem statement<br>- Evaluate the responses for groundedness and relevance<br>- Provide comments/observations for the answers received | 3 |
| **Data Preparation for RAG** | - Load the data file provided<br>- Split the data using a text splitter with the necessary attributes<br>- Load the embedding model<br>- Load the vector database<br>- Define the retriever with an appropriate search method and k value<br>- Test the retriever by fetching relevant chunks of data as per the provided questions | 7 |
| **Question Answering using RAG** | - Apply the response generation function to get answers to the questions provided in the problem statement<br>- Evaluate the responses for groundedness and relevance<br>- Provide comments/observations for the answers received | 10 |
| **Question Answering using RAG Fine Tuning** | - Tune the hyperparameters of the RAG system (try 5 combinations at least)<br>- Apply the response generation function to get answers to the provided questions using each combination above<br>- Evaluate the responses for groundedness and relevance<br>- Provide comments/observations for the answers received | 25 |
| **Actionable Insights and Recommendations** | - Compare and comment on the performance of all the methods tried so far<br>- Key takeaways for the business | 4 |
| **Business Report Quality** | - Adhere to the business report checklist | 6 |

---

## Project Structure
```
flykite-hr-assistant/
├── README.md
├── requirements.txt
├── data/
│   └── employee_handbook.pdf
├── notebooks/
│   ├── interim_report.ipynb
│   └── final_report.ipynb
├── src/
│   ├── llm_setup.py
│   ├── data_preparation.py
│   ├── rag_pipeline.py
│   ├── evaluator.py
│   └── utils.py
├── embeddings/
│   └── vector_store/
└── docs/
    └── business_report.md
```

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/flykite-hr-assistant.git
cd flykite-hr-assistant

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

## Usage

### Basic Query Example
```python
from src.rag_pipeline import HRPolicyAssistant

# Initialize the assistant
assistant = HRPolicyAssistant()

# Ask a question
question = "What are the effects on benefits if probation is extended?"
response = assistant.query(question)

print(response['answer'])
print(f"Source: {response['source']}")
```

### RAG Pipeline Setup
```python
from src.data_preparation import prepare_documents
from src.rag_pipeline import build_rag_pipeline

# Prepare documents
chunks = prepare_documents('data/employee_handbook.pdf')

# Build RAG pipeline
rag_chain = build_rag_pipeline(chunks)

# Query the system
result = rag_chain.invoke("How do I apply for bereavement leave?")
```

## Technologies Used

- **Python 3.8+**
- **LangChain** - RAG framework
- **OpenAI GPT / Anthropic Claude** - Large Language Models
- **Hugging Face Transformers** - Embedding models
- **FAISS / ChromaDB** - Vector databases
- **PyPDF2 / PDFPlumber** - PDF processing
- **Pandas & NumPy** - Data manipulation

## Key Features

- 📚 **Document Processing**: Efficiently processes HR policy PDFs
- 🔍 **Semantic Search**: Retrieves relevant policy sections using vector embeddings
- 💬 **Context-Aware Responses**: Generates accurate answers grounded in source documents
- 📝 **Source Attribution**: Cites specific sections and clauses from policy documents
- ⚙️ **Hyperparameter Tuning**: Optimizable RAG pipeline for best performance
- 📊 **Evaluation Metrics**: Groundedness and relevance scoring

## RAG System Components

### 1. Document Loading & Chunking
- Load PDF employee handbook
- Split into manageable chunks using appropriate text splitters
- Preserve context and section boundaries

### 2. Embedding & Vector Storage
- Generate embeddings using state-of-the-art models
- Store in vector database (FAISS/ChromaDB)
- Enable fast similarity search

### 3. Retrieval
- Implement semantic search with configurable k value
- Support multiple search methods (similarity, MMR, etc.)
- Return relevant document chunks

### 4. Generation
- Use LLM to generate responses based on retrieved context
- Apply prompt engineering for better outputs
- Include source citations

## Evaluation Metrics

- **Groundedness**: How well the answer is supported by retrieved documents
- **Relevance**: How well the answer addresses the user's question
- **Source Attribution**: Accuracy of citations and references

## Hyperparameter Tuning

The RAG system supports tuning of:
- Chunk size and overlap
- Number of retrieved documents (k)
- Embedding model selection
- Retrieval algorithm (similarity, MMR, etc.)
- LLM temperature and parameters

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please contact: [your-email@example.com]

## Acknowledgments

- Flykite Airlines for providing the employee handbook dataset
- LangChain community for RAG framework
- OpenAI/Anthropic for LLM APIs
