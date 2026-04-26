# Q5: RAG Chatbot from PDF
# Task: Build a chatbot that answers questions from a PDF document
# Stack: LangChain + ChromaDB + Ollama (local LLM)
# Install: pip install langchain chromadb pypdf sentence-transformers
# Ollama: https://ollama.ai -> ollama pull mistral
# Docs: https://python.langchain.com/docs/use_cases/question_answering/

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

PDF_PATH = "document.pdf"
DB_PATH = "chroma_db"

def load_and_index(pdf_path):
    print("Loading PDF...")
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(pages)
    print(f"Created {len(chunks)} chunks")

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(chunks, embeddings, persist_directory=DB_PATH)
    db.persist()
    print("Indexed and saved to ChromaDB")
    return db

def create_qa_chain(db):
    llm = Ollama(model="mistral")
    retriever = db.as_retriever(search_kwargs={"k": 3})
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa

def chat(qa_chain):
    print("RAG Chatbot ready. Type quit to exit.")
    while True:
        query = input("You: ")
        if query.lower() == "quit":
            break
        answer = qa_chain.run(query)
        print(f"Bot: {answer}
")

db = load_and_index(PDF_PATH)
qa_chain = create_qa_chain(db)
chat(qa_chain)