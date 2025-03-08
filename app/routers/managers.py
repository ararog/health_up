from fastapi import APIRouter
from app.models import Manager
from app.services.managers import (
    get_managers, 
    create_manager, 
    update_manager
)

router = APIRouter(
    prefix="/managers",
    tags=["managers"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["managers"])
async def handle_get_managers() -> list[Manager]:
    return get_managers()

@router.post("/", tags=["manager"])
async def handle_create_manager(manager: Manager):
    return create_manager(manager)

@router.put("/{id}", tags=["manager"])
async def handle_update_manager(id: str, manager: Manager):
    return update_manager(id, manager)

