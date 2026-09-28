"""Step 6  : connect to the llm(the brain)"""

from langchain_groq import ChatGroq
from hr_assistant import config

def get_llm():
    """Return a Groq chat model"""
    return ChatGroq(model=config.LLM_MODEL_NAME , temperature=0)

