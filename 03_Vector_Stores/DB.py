from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


# 1. Sample documents
documents = [
    Document(page_content="Python is a programming language."),
    Document(page_content="Machine Learning allows computers to learn from data."),
    Document(page_content="RAG combines document retrieval with a language model."),
]


# 2. Create embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# 3. Create vector store
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="chroma_db"
)


# 4. Search
results = vector_store.similarity_search(
    "What is machine learning?",
    k=2
)


# 5. Print results
for doc in results:
    print(doc.page_content)
