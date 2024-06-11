import json
import requests
from typing import Type, Optional
from pydantic.v1 import BaseModel, Field
from crewai_tools import BaseTool


class SunoToolSchema(BaseModel):
    """Input for SunoTool"""
    url: str = Field(..., description="URL for the Suno API. This field is mandatory")
    genre: str = Field(..., description="The song genre. E.g. Hip Hop, Rap, Pop, etc.")
    

class SunoTool(BaseTool):
    name: str = "Generate a song from the lyrics"
    description: str = "A tool that can be used to generate a song from the provided lyrics."
    args_schema: Type[BaseModel] = SunoToolSchema
    url: str = ""
    genre: str = ""
    
    def __init__(self, url: str, genre: str, **kwargs):
        super().__init__(**kwargs)
        self.url = f"{url}/api/custom_generate"
        self.genre = genre
        
        
    def download_audios(self, audio_url: str, audio_id: int):
        response = requests.get(audio_url, stream=True)
        save_path = f"./{audio_id}.mp3"
        
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
        else:
            raise ValueError("Invalid URL, the audio can't be downloaded")
        
    def _run(
        self,
        lyrics: str,
        **kwargs
    ):
        payload = {
            "prompt": lyrics,
            "tags": self.genre,
            "title": "Generated Song",
            "make_instrumental": False,
            "wait_audio": True
        }
        try:
            response = requests.post(self.url, json=payload, headers={'Content-Type': 'application/json'})
            audio_info = response.json()
        except Exception as e:
            raise ValueError(e)
        
        self.download_audios(audio_url=audio_info[0].get("audio_url"), audio_id=1)
        self.download_audios(audio_url=audio_info[1].get("audio_url"), audio_id=2)
        
        return "Audios successfully downloaded"
