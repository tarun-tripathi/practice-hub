# Q9: Semantic Search over Google Drive Documents
# Task: Search your Google Drive docs using semantic similarity
# Tools: LangChain + ChromaDB + Google Drive API
# Install: pip install langchain chromadb sentence-transformers google-api-python-client
# Auth setup: https://developers.google.com/drive/api/quickstart/python

from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
DB_PATH = "semantic_search_db"

def authenticate_google():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as f:
            f.write(creds.to_json())
    return build("drive", "v3", credentials=creds)

def fetch_docs(service):
    results = service.files().list(
        q="mimeType='application/vnd.google-apps.document'",
        fields="files(id, name)"
    ).execute()
    return results.get("files", [])

def index_documents(docs_text):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    documents = [Document(page_content=text["content"], metadata={"name": text["name"]})
                 for text in docs_text]
    db = Chroma.from_documents(documents, embeddings, persist_directory=DB_PATH)
    db.persist()
    print(f"Indexed {len(documents)} documents")
    return db

def search(db, query, k=3):
    results = db.similarity_search(query, k=k)
    print(f"
Results for: {query}")
    for i, doc in enumerate(results):
        print(f"
{i+1}. {doc.metadata.get('name', 'Unknown')}")
        print(f"   {doc.page_content[:200]}...")

# Note: Set up Google Drive API credentials first
# Download credentials.json from Google Cloud Console
# Then uncomment and run:
# service = authenticate_google()
# files = fetch_docs(service)
# print(f"Found {len(files)} Google Docs")
print("Setup Google Drive API credentials to use this feature.")
print("Guide: https://developers.google.com/drive/api/quickstart/python")