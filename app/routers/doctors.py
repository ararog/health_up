from fastapi import APIRouter
from app.models import Doctor
from app.services.doctors import (
    get_doctors, 
    create_doctor, 
    update_doctor
)

router = APIRouter(
    prefix="/doctors",
    tags=["doctors"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["doctors"])
async def handle_get_doctors() -> list[Doctor]:
    return get_doctors()

@router.post("/", tags=["doctor"])
async def handle_create_doctor(doctor: Doctor):
    return create_doctor(doctor)

@router.put("/{id}", tags=["doctor"])
async def handle_update_doctor(id: str, doctor: Doctor):
    return update_doctor(id, doctor)

