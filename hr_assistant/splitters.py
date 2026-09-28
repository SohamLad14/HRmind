""" Step 2 : Split the text into smaller data chunks"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from hr_assistant import config

def split_into_chunks(documents):
    """Split documents into small overlapping chunks"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = config.CHUNK_SIZE,
        chunk_overlap = config.CHUNK_OVERLAP
    )
    return text_splitter.split_documents(documents)
