import warnings
warnings.filterwarnings("ignore")
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# 1. Load text file
loader = TextLoader("notes.txt", encoding="utf-8")
docs = loader.load()

# 2. Create Hugging Face LLM
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# 3. Get text from document
document_text = docs[0].page_content

# 4. Ask question using document content
question = input("Enter your question: ")

prompt = f"""
Answer the question using the following document.

Document:
{document_text}

Question:
{question}
"""

# 5. Invoke model
response = model.invoke(prompt)

# 6. Print answer
print(response.text)