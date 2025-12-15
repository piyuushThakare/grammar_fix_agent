# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from agent import GrammarAgent

app = FastAPI(
    title="Grammar Fix Agent API",
    description="AI-powered grammar correction service",
    version="1.0"
)

# Load model once at startup
agent = GrammarAgent()

class GrammarRequest(BaseModel):
    sentence: str

class GrammarResponse(BaseModel):
    corrected_sentence: str

@app.post("/correct", response_model=GrammarResponse)
def correct_grammar(request: GrammarRequest):
    corrected = agent.correct(request.sentence)
    return {"corrected_sentence": corrected}
