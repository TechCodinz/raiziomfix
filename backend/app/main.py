from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables from .env if present
load_dotenv(Path(__file__).resolve().parents[2] / '.env')

API_BASE = os.getenv('API_BASE', 'https://api.example.com')
SECRET_KEY = os.getenv('SECRET_KEY', 'change-me')

app = FastAPI()

class Idea(BaseModel):
    idea: str

class Message(BaseModel):
    input: str

@app.get('/')
def read_root():
    return {'message': 'RaiziomFix API'}

@app.post('/idea')
def receive_idea(idea: Idea):
    # Placeholder for storing idea or forwarding to a service
    return {'received': idea.idea}

@app.post('/ai/respond')
def ai_respond(message: Message):
    reply = f"Echo from {API_BASE}: {message.input}"
    return {'reply': reply}
