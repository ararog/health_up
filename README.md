# Health Up

A quick and easy way to schedule your health appointments.

## License

MIT

## Requirements

Python 3.6
PostgreSQL 16.0
uv
ngrok or loclx

## Installation

### Clone the repository: 

```bash
git clone https://github.com/ararog/health_up.git
```

### Update the .env file:

```plaintext
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_NUMBER=
DB_SERVER=
DB_NAME=
OPENAI_API_KEY=
TO_NUMBER=
```

### Server setup:

1. Create a Twilio account and get your account SID and auth token.
2. Update the .env file with your Twilio account SID, auth token, and twilio phone number, your phone number, and openai api key.

## Starting server

```bash
cd health_up
uv sync
uv run fastapi run
```

## Starting ngrok or loclx
```bash
ngrok http 8000
```
or

```bash
loclx http 8000
```

## Update the webhook URL in your Twilio account to the ngrok or loclx URL.

1. In twillio console, go to Develop tab
2. Click on Messaging - Try it out - Send a whatsapp message
3. Click on Sandbox Settings
4. On [When a message comes in] field, enter the ngrok or loclx URL with /messages appended to the end.

## Testing

Open your whatsapp and send a message to your twilio number.