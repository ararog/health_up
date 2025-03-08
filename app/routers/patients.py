from fastapi import APIRouter
from app.models import Patient
from app.services.patients import (
    get_patients, 
    create_patient, 
    update_patient
)

router = APIRouter(
    prefix="/patients",
    tags=["patients"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["patients"])
async def handle_get_patients() -> list[Patient]:
    return get_patients()
  
@router.post("/", tags=["patients"])
async def handle_create_patient(patient: Patient):
    return create_patient(patient)

@router.put("/{id}", tags=["patients"])
async def handle_update_patient(id: str, patient: Patient):
    return update_patient(id, patient)
