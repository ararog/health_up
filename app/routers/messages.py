import pprint
import openai
import logging
from fastapi import APIRouter, Form, Depends
from decouple import config
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

def send_message(client: Client, to_number, body_text):
  try:
      max_length = 1600
      # Calculate the number of messages
      num_messages = len(body_text) // max_length + (1 if len(body_text) % max_length > 0 else 0)
      
      print(client.password)
    
      for i in range(num_messages):
          # Calculate start and end indices for the substring
          start_index = i * max_length
          end_index = start_index + max_length

          # Get the substring for the current chunk
          message_chunk = body_text[start_index:end_index]
          
          # Send the chunk as a message
          message = client.messages.create(
              from_=f"whatsapp:{twilio_number}",
              body=message_chunk,
              to=f"whatsapp:{to_number}"
          )

          logger.info(f"Message {i + 1}/{num_messages} sent from {twilio_number} to {to_number}: {message.sid}")

  except Exception as e:
      logger.error(f"Error sending message to {to_number}: {e}")

@router.post("/")
async def handle_message(Body: str = Form(), 
                         twillio_client: Client = Depends(get_twilio_client), 
                         openai_client: openai.OpenAI = Depends(get_openai_client)):
  chat_response = "no data"
  response = openai_client.chat.completions.create(
      model="gpt-4-turbo",
      messages=[{"role": "system", "content": "Your system message here, if any"},
                {"role": "user", "content": Body}],
      stream=False
  )

  if response.choices and response.choices[0].message.content:
      chat_response = response.choices[0].message.content
  
  send_message(twillio_client, whatsapp_number, chat_response)
  #insert_text_into_db(whatsapp_number, Body, chat_response)
  return ""
