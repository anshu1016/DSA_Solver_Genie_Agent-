import os
from dotenv import load_dotenv
load_dotenv()

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent,CodeExecutorAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

api_key = os.getenv('GROQ_API_KEY_1')

model_client = OpenAIChatCompletionClient(
    model="llama3-70b-8192",
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
    model_info={
        "family": "llama",
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True
    },
    default_params={
        "temperature": 1
    }
)

def get_model_client():
    model_client = OpenAIChatCompletionClient(
    model="llama3-70b-8192",
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
    model_info={
        "family": "llama",
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True
    },
    default_params={
        "temperature": 1
    }
)

    return model_client