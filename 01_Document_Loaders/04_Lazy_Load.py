import warnings 
warnings .filterwarnings('ignore')
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
loader =DirectoryLoader(
    path = 'Book',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)

docs = loader.lazy_load()
# print(len(docs))
for document in docs :
    print(document.metadata)