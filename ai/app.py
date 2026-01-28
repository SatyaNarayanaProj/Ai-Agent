from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from modeling import generate_description , generate_suggestions , generate_completion


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- MODELS ----------
class RequestBody(BaseModel):
    title: str


# ---------- SUGGESTIONS ----------
@app.get("/suggest")
def suggest(q: str):
    suggestions = generate_suggestions(q)
    return {"suggestions": suggestions}


# ---------- GENERATION ----------
@app.post("/generate")
def generate(req: RequestBody):
    description = generate_description(req.title)
    return {"description": description}


@app.get("/autocomplete")
def autocomplete(q: str):
    return {"completion": generate_completion(q)}
