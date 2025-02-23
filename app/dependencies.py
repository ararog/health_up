import openai
from typing import Annotated
from fastapi import Depends
from decouple import config
from twilio.rest import Client

account_sid = config("TWILIO_ACCOUNT_SID")
auth_token = config("TWILIO_AUTH_TOKEN")

def get_twilio_client():
  return Client(account_sid, auth_token)

def get_openai_client():
  return openai.OpenAI(api_key=config("OPENAI_API_KEY"))
