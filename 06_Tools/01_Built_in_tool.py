from dotenv import load_dotenv
load_dotenv()

from langchain_community.tools import TavilySearchResults
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# 1. Create Hugging Face LLM
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)


# 2. Create Tavily search tool
search_tool = TavilySearchResults(max_results=5)


# 3. Create prompt
prompt = ChatPromptTemplate.from_template(
    """
You are a helpful assistant.

Summarize the following news into clear bullet points.

News:
{news}
"""
)


# 4. Create chain
chain = prompt | model | StrOutputParser()


# 5. Search the web
news_result = search_tool.invoke(
    {"query": "Latest AI news of 2026"}
)


# 6. Summarize the search results
result = chain.invoke(
    {"news": news_result}
)


# 7. Print result
print(result)


# 8. Print tool information
print("\nTool description:")
print(search_tool.description)

print("\nTool name:")
print(search_tool.name)

print("\nTool arguments:")
print(search_tool.args)