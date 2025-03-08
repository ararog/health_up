from fastapi import APIRouter
from app.models import Speciality
from app.services.specialities import (
  get_specialities, 
  create_speciality, 
  update_speciality
)

router = APIRouter(
    prefix="/specialities",
    tags=["specialities"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["specialities"])
async def handle_get_specialities() -> list[Speciality]:
    return get_specialities()

@router.post("/", tags=["specialities"])
async def handle_create_speciality(speciality: Speciality):
    return create_speciality(speciality)

@router.put("/{id}", tags=["specialities"])
async def handle_update_speciality(id: str, speciality: Speciality):
    return update_speciality(id, speciality)

