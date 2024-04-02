!pip install langchain
!pip install openai==0.28
!pip install chromadb==0.3.29
!pip install tiktoken
!pip install pypdf

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.chains import VectorDBQA, RetrievalQA
from langchain.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import openai

doc_loader = DirectoryLoader('Python',glob="./*.pdf",loader_cls=PyPDFLoader)
hrdocument = doc_loader.load()
hrdocument

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 0)
texts = text_splitter.split_documents(hrdocument)

api_key = "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"
openai_embeddings = OpenAIEmbeddings(openai_api_key = api_key)
embedding = openai_embeddings
vectordb = Chroma.from_documents(documents = texts,
                                 embedding=embedding,
                                 persist_directory="Py_Basics")

from io import open_code
gptllm = ChatOpenAI(model_name = 'gpt-3.5-turbo', openai_api_key = api_key, temperature = 0)

qa = RetrievalQA.from_chain_type(llm = gptllm,
                                 chain_type = "stuff",
                                 retriever = vectordb.as_retriever())

while True:
  prompt = input("\nAsk Anything: ")
  if prompt == 'Exit':
    break
  if prompt.strip()=="":
    continue
  res = qa(prompt)
  print("\n\n Question:")
  print(prompt)
  print(f"\n> Response:")
  print(res['result'])
