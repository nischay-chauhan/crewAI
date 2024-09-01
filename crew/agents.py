from crewai import Agent
from dotenv import load_dotenv

load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="" , verbose=True , temprature=0.5 , google_api_key = os.getenv("GOOGLE_API_KEY"))

# reasearch agent

news_researcher = Agent(
    role="Senior Researcher",
    goal='Uncover theground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backStory=(
        "Driven by curiosity , you're at the forefront of innovation , eager to explore "
        "the latest and greatest in technology. "
    ),
    tools=[],
    llm=llm,
    allow_delegation=True

)

# creating a writer agent

news_write = Agent(
    role="Writer",
    goal='Narrate compelling tech stories about  {topic}',
    verbose=True,
    memory=True,
    backStory=(
        "with a flair for simplicity and clarity"
        "and a passion for writing"
        "and a desire to share"
    ),
    tools=[],
    llm=llm,
    allow_delegation=False
)

