"""Step 4 : Store chunks in embeddings so we can search them"""

import os
from langchain_community.vectorstores import FAISS
from hr_assistant import config
from hr_assistant.embeddings import get_embedding_model

def build_vector_store(chunks):
    """Embed every chunk and build a searchable FAISS index and memory"""
    embedding_model = get_embedding_model()
    return FAISS.from_documents(chunks , embedding_model)

## save vector store

def save_vector_store(vector_store ,path : str = config.VECTOR_STORE_PATH) -> None:
    """Save the FAISS index to disk so we dont have to rebuild it every time"""
    vector_store.save_local(path)

def load_vector_store(path : str = config.VECTOR_STORE_PATH):
    """Load a previously saved FAISS index from disk."""
    embedding_model = get_embedding_model()
    return FAISS.load_local(path , embedding_model , allow_dangerous_deserialization= True)

#what if vector store does not exists

def vector_store_exists(path : str = config.VECTOR_STORE_PATH) -> bool:
    """Check if a save FAISS index already exits on disk"""
    return os.path.exists(os.path.join(path , "index.faiss"))

def get_retriever(vector_store , k : int = config.TOP_K_RESULTS):
    """Turn a vector store into a retriever that returns the top-k matching chunks"""
    return vector_store.as_retriever(search_kwarfs = {"k" : k})

