""" step 3 : Turn text into numbers using JINA"""

from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def get_embedding_model():
    """ return a JINA embedding model"""
    logger.info("Initiakizing embeddings model '%s'", config.EMBEDDING_MODEL_NAME)
    return JinaEmbeddings(model_name = config.EMBEDDING_MODEL_NAME)