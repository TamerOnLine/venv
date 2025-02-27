import os
import requests
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool