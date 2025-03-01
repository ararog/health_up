from fastapi import FastAPI, Depends
from decouple import config
from .routers import messages, medias
from .dependencies import get_kafka_producer

server = config('DB_SERVER')
database = config('DB_NAME')

app = FastAPI()

app.include_router(medias.router)
app.include_router(messages.router, 
                   dependencies=[
                     Depends(get_kafka_producer)
                  ])

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
