from typing import Annotated
from fastapi import APIRouter, Path
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/medias",
    tags=["medias"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{audio_file}", status_code=200)
async def handle_media(audio_file: Annotated[str, Path(title="Audio file to reply")]):
  return FileResponse(audio_file)