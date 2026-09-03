import os
from dotenv import load_dotenv

load_dotenv()

# --- LLM ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = "openai/gpt-oss-120b"

# --- Embeddings ---
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# --- Vector store ---
# Changed the collection name to reflect our new domain
CHROMA_COLLECTION = "handgun_maintenance"
CHROMA_PATH = "./chroma_db"

# --- Retrieval ---
N_RESULTS = 4

# --- Documents ---
DOCS_PATH = "./docs"