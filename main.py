from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/add")
async def add_url(nameURL: URLRequest):     # nameURL: URLRequest --> Tem que seguir o formato da clase 
    return {"url": nameURL.url}

@app.get("/health")
def statsOk():
    return {"status": "ok"}