import openai
import logging
from typing import Annotated
from fastapi import APIRouter, Form, Depends
from decouple import config
from twilio.rest import Client
from ..services.media import transcribe_media
from ..services.messaging import send_reply
from ..dependencies import get_twilio_client, get_openai_client

twilio_number = config('TWILIO_NUMBER')
whatsapp_number = config("TO_NUMBER")

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
                         twilio_client: Client = Depends(get_twilio_client), 
                         openai_client: openai.OpenAI = Depends(get_openai_client)):
  
  message = Body
  num_media = int(NumMedia or 0)
  if num_media > 0:
      media_url = MediaUrl0
      mime_type = MediaContentType0
      message = transcribe_media(media_url, mime_type, twilio_client, openai_client)
  
  chat_response = "no data"
  response = openai_client.chat.completions.create(
      model="gpt-4-turbo",
      messages=[{"role": "system", "content": "Your system message here, if any"},
                {"role": "user", "content": message}],
      stream=False
  )

  if response.choices and response.choices[0].message.content:
      chat_response = response.choices[0].message.content
  
  send_reply(From, chat_response, num_media > 0, response.id, twilio_client, openai_client)
  
  #insert_text_into_db(whatsapp_number, Body, chat_response)
  
  return { "status": "success" }
