""" step 3 : Turn text into numbers using JINA"""

from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config

def get_embedding_model():
    """ return a JINA embedding model"""
    return JinaEmbeddings(model_name = config.EMBEDDING_MODEL_NAME)