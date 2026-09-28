#All setting for the app lives here

import os 
from dotenv import load_dotenv

load_dotenv()

#ENV VAR/SECRET

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")

#DEFINE PATH - DATA/VECTOR STORE
DATA_FILE_PATH = os.path.join("data" , "hr_policy.txt")

#VECTOR STORES

VECTOR_STORE_PATH = os.path.join("data" , "faiss_index")

#MODELS
##LLM and Embeddings

LLM_MODEL_NAME = "openai/gpt-oss-20b"

EMBEDDING_MODEL_NAME = "jina-embeddings-v2-base-en"

##CHUNKS / TEXT SPLITTING CONGIF

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

#RETIREVAL RESULTS
TOP_K_RESULTS = 3

## SYSTEM INSTRUCTIONS 

SYSTEM_PROMPT = (
    "You are a friendly HR assistant. Always use the search_hr_policy tool to look up "
    "facts before answering. If the answer isn't in the search results, say you don't know "
    "instead of guessing."
)


#CHECK IF API KEY EXITS OR NOT

def check__api()-> None:
    """Stop early with a clear message if a required API key is Missing """

    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY. Please add it to your .env file.")
    if not JINA_API_KEY:
        raise ValueError("Missing Jina_API_KEY. Please add it to your .env file")


