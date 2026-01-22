from fastapi import FastAPI
from pydantic import BaseModel
from model import generate_description
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestBody(BaseModel):
    title: str

@app.post("/generate")
def generate(req: RequestBody):
    try:
        description = generate_description(req.title)
        return {"description": description}
    except Exception as e:
        return {"error": str(e)}
