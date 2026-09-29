"""Step 7 : Build the agent that ties the LLm and the search tool togther"""

from langchain.agents import create_agent
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def create_hr_agent(llm ,tools):
    """Return a Langchain agent that can call our tools to ansswer questions"""
    logger.info("Creating HR agent with %d tool(s)" , len(tools))
    agent = create_agent(model = llm ,tools = tools , system_prompt= config.SYSTEM_PROMPT)
    logger.info("HR agent ready")
    return agent