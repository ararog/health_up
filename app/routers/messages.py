import logging
from typing import Annotated
from fastapi import APIRouter, Form, Depends
from decouple import config
from kafka import KafkaProducer

from ..dependencies import get_kafka_producer

router = APIRouter(
    prefix="/messages",
    tags=["messages"],
    responses={404: {"description": "Not found"}},
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/", status_code=201)
async def handle_message(From: Annotated[str | None, Form()] = None, Body: str = Form(),
                         NumMedia: Annotated[str | None, Form()] = None,
                         MediaUrl0: Annotated[str | None, Form()] = None, 
                         MediaContentType0: Annotated[str | None, Form()] = None,
                         kafka_producer: KafkaProducer = Depends(get_kafka_producer)):

  kafka_producer.send(topic="process_message", 
                      value={"body": Body,
                             "from_number": From,
                             "num_media": NumMedia,
                             "media_url": MediaUrl0, 
                             "media_type": MediaContentType0})
  
  return { "status": "success" }
