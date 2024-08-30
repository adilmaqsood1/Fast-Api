from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, World!"}

@app.get("/home")
def home():
    return {"message": "Welcome to home page"}