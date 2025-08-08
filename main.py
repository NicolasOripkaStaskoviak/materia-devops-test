import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def functeste():
    return {"teste": "deu certo", "numero_aleatorio": random.randint(0,100)}