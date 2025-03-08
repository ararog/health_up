from fastapi import APIRouter
from app.models import User
from app.services.users import create_user, update_user, get_users

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["users"])
async def handle_get_users():
    return get_users()

@router.post("/", tags=["users"])
async def handle_create_user(user: User):
    create_user(user)

@router.put("/{id}", tags=["users"])
async def handle_update_user(id: str, user: User):
    update_user(id, user)
