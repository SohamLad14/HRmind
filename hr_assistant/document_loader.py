"""Step 1 : Read the raw document from the data folder"""

from langchain_community.document_loaders import TextLoader
from hr_assistant import config

def load_document(file_path : str = config.DATA_FILE_PATH):
    """Load  a .txt file and return it as a list of Langchain Document Objects"""
    loader = TextLoader(file_path , encoding= 'utf-8')
    document = loader.load()
    return document    