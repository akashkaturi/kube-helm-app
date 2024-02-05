import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "Bhavana Bhawdhane", "Env": os.environ}
