from fastapi import APIRouter
from app.models import Appointment
from app.services.appointments import (
    create_appointment, 
    update_appointment, 
    get_appointments
)

router = APIRouter(
    prefix="/appointments",
    tags=["appointments"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["appointments"])
async def handle_get_appointments() -> list[Appointment]:
    return get_appointments()

@router.post("/", tags=["appointments"])
async def handle_create_appointment(appointment: Appointment):
    return create_appointment(appointment)

@router.put("/{id}", tags=["appointments"])
async def handle_update_appointment(id: str, appointment: Appointment):
    return update_appointment(id, appointment)
