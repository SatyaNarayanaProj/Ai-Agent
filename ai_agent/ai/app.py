from fastapi import FastAPI
from pydantic import BaseModel
from model import generate_description, generate_suggestions
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestBody(BaseModel):
    title: str


@app.get("/suggest")
def suggest(q: str):
    return {"suggestions": generate_suggestions(q)}


@app.post("/generate")
def generate(req: RequestBody):
    return {"description": generate_description(req.title)}
