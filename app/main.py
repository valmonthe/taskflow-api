from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "TaskFlow API"}

def hello():
    x = 5
    print("hello")