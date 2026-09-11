from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from tiktoken import model

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

url = "https://www.youtube.com/watch?v=bL92ALSZ2Cg&list=PLKnIA16_Rmva0dRLWEHLznSHKbFD_RJfX&index=3"
loader = WebBaseLoader(url)
docs = loader.load()

print(len(docs))
print(docs[0].page_content)

# 4. Ask question using document content
question = input("Enter your question: ")

prompt = f"""
Answer the question using the following document.
Question:
{question}
"""


# 5. Invoke model
response = model.invoke(prompt)

# 6. Print answer
print(response.text)