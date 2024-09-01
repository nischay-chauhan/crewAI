from crewai import Agent
from dotenv import load_dotenv

load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="" , verbose=True , temprature=0.5 , google_api_key = os.getenv("GOOGLE_API_KEY"))