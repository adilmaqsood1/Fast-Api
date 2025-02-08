from fastapi import FastAPI 
import pydantic

app = FastAPI()

@app.get("/{name}")
def name(name :str):
    return {"name": name}


