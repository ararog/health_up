from fastapi import FastAPI, Depends
from decouple import config
from .routers import messages
from .dependencies import get_twilio_client, get_openai_client

server = config('DB_SERVER')
database = config('DB_NAME')

app = FastAPI()

app.include_router(messages.router, dependencies=[Depends(get_twilio_client), Depends(get_openai_client)])

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
