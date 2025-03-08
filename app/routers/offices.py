from fastapi import APIRouter
from app.models import Office
from app.services.offices import get_offices, create_office, update_office

router = APIRouter(
    prefix="/offices",
    tags=["offices"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["offices"])
async def handle_get_offices() -> list[Office]:
    return get_offices()

@router.post("/", tags=["office"])
async def handle_create_office(office: Office):
    return create_office(office)

@router.put("/{id}", tags=["office"])
async def handle_update_office(id: str, office: Office):
    return update_office(id, office)

