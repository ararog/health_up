from fastapi import FastAPI, Depends
from .routers import auth, messages, medias, offices, patients, users, doctors, specialities, appointments
from .dependencies import get_kafka_producer

app = FastAPI()

app.include_router(auth.router)
app.include_router(offices.router)
app.include_router(users.router)
app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(specialities.router)
app.include_router(appointments.router)
app.include_router(medias.router)
app.include_router(messages.router, 
                   dependencies=[
                     Depends(get_kafka_producer)
                  ])

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
