from langchain_community.document_loaders import PyPDFLoader
import warnings 
warnings.filterwarnings("ignore")
# Load PDF
loader = PyPDFLoader("GRU.pdf")

# Read PDF
docs = loader.load()

# Check pages
print("PDF loaded successfully!")
print("Number of pages:", len(docs))

# Show first page
print("\nFirst page content:")
print(docs[0].page_content)

# Show metadata
print("\nMetadata:")
print(docs[0].metadata)