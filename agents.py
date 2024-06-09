import os
from textwrap import dedent

from dotenv import load_dotenv
from crewai import Agent
from langchain_groq import ChatGroq

load_dotenv()

llama3_70b = ChatGroq(api_key=os.environ.get("GROQ_API_KEY"), model="llama3-70b-8192")


class MelodyAgents:
    
    def __init__(self, llm):
        self.llm = llm
        
        
    def web_researcher_agent(self):
        return Agent(
            role="Web Researcher",
            goal="Conducts a web search on a topic, generating a detailed report on the matter",
            tools = [],
            backstory=dedent(
                "An expert in conducting web researchs about any topic"
            ),
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def lyrics_creator_agent(self):
        return Agent(
            role="Lyrics Creator",
            goal=dedent("""Create the most amazing lyrics about a topic
                        adapting the writing style to the music genre."""),
            backstory="A creative lyricist who excels at creating high quality lyrics",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
