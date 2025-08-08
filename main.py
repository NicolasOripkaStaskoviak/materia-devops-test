from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/functeste")
async def functeste():
    return {"teste": "deu certo"}