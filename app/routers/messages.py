import os
import mimetypes
import requests
import openai
import logging
from typing import Annotated
from fastapi import APIRouter, Form, Depends
from decouple import config
from urllib.parse import urlparse
from twilio.rest import Client
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

def send_message(twilio_client: Client, to_number, body_text):
  try:
      max_length = 1600
      # Calculate the number of messages
      num_messages = len(body_text) // max_length + (1 if len(body_text) % max_length > 0 else 0)
    
      for i in range(num_messages):
          # Calculate start and end indices for the substring
          start_index = i * max_length
          end_index = start_index + max_length

          # Get the substring for the current chunk
          message_chunk = body_text[start_index:end_index]
          
          # Send the chunk as a message
          message = twilio_client.messages.create(
              from_=f"whatsapp:{twilio_number}",
              body=message_chunk,
              to=to_number
          )

          logger.info(f"Message {i + 1}/{num_messages} sent from {twilio_number} to {to_number}: {message.sid}")

  except Exception as e:
      logger.error(f"Error sending message to {to_number}: {e}")

def transcribe_media(media_url, mime_type, twilio_client: Client, openai_client: openai.OpenAI):
  
  file_extension = mimetypes.guess_extension(mime_type)
  media_sid = os.path.basename(urlparse(media_url).path)
  content = requests.get(
    media_url, 
    auth=(twilio_client.account_sid, twilio_client.password), 
    stream=True
  ).raw.read()
  filename = '{sid}{ext}'.format(sid=media_sid, ext=file_extension)
  with open(filename, 'wb') as fd:
    fd.write(content)
  
  response = openai_client.audio.transcriptions.create(
      model="whisper-1",
      file=open(filename, "rb"),
      response_format="text"
  )
  return response

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
  
  send_message(twilio_client, From, chat_response)
  
  #insert_text_into_db(whatsapp_number, Body, chat_response)
  
  return { "status": "success" }
