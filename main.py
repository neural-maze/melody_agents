from crewai import Crew
from textwrap import dedent
from agents import MelodyAgents
from tasks import MelodyTasks

from dotenv import load_dotenv
load_dotenv()


class MelodyCrew:
    def __init__(self, topic: str, genre: str):
        self.topic = topic
        self.genre = genre
        
    def run(self):
        agents = MelodyAgents()
        tasks = MelodyTasks()
        
        web_researcher_agent = agents.web_researcher_agent()
        lyrics_creator_agent = agents.lyrics_creator_agent()
        
        web_research_task = tasks.web_research_task(
            agent=web_research_task, 
            topic=self.topic
        )
        lyrics_creation_task = tasks.lyrics_creation_task(
            agent=lyrics_creator_agent, 
            topic=self.topic, 
            genre=self.genre
        )
        
        crew = Crew(
            agents=[
                web_researcher_agent,
                lyrics_creator_agent
            ],
            tasks=[
                web_research_task,
                lyrics_creation_task
            ],
            verbose=True
        )
                
        return crew.kickoff()
        
        

if __name__ == "__main__":
    topic = input(
        "What's the topic of the song?"
    )
    genre = input(
        "What's the music genre? Hip Hop, Rap, K-Pop, etc."
    )
    
    melody_crew = MelodyCrew(topic, genre)
    print(melody_crew.run())
