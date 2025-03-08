from fastapi import APIRouter
from app.models import Owner
from app.services.owners import (
    get_owners, 
    create_owner, 
    update_owner
)

router = APIRouter(
    prefix="/owners",
    tags=["owners"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["owners"])
async def handle_get_owners() -> list[Owner]:
    return get_owners()

@router.post("/", tags=["owner"])
async def handle_create_owner(owner: Owner):
    return create_owner(owner)

@router.put("/{id}", tags=["owner"])
async def handle_update_owner(id: str, owner: Owner):
    return update_owner(id, owner)

