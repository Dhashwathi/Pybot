# Pybot - Content Generator
Pybot is a Python project aimed at generating conversational responses and answering questions based on provided documents which are related to python. It utilizes various libraries and APIs for natural language processing and document analysis.

# Installation
You can install the required dependencies using pip:\
    pip install langchain\
    pip install openai==0.28\
    pip install chromadb==0.3.29\
    pip install tiktoken\
    pip install pypdf

# Usage
**Document Loading:** The project starts by loading documents from a specified directory. It supports loading PDF files using PyPDFLoader.

**Text Processing:** The loaded documents are split into smaller text chunks for better processing. RecursiveCharacterTextSplitter is used for this purpose.

**Embeddings Generation:** OpenAI's GPT model is used to generate embeddings for the text chunks. This helps in understanding the context of the text.

**Vectorization:** The text chunks are then vectorized using Chroma, a vector storage library. This step facilitates efficient retrieval of relevant information.

**Question Answering:** The project sets up a conversational interface using OpenAI's GPT-3.5 model. Users can ask questions, and the system retrieves relevant answers based on the preprocessed documents.
![Screenshot (676)](https://github.com/Dhashwathi/Pybot/assets/127650913/76cd9843-053f-4d44-8ae2-068ade037e94)

# Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.
