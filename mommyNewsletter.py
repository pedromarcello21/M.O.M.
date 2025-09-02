from dotenv import load_dotenv
import openai
import json
import os
#layer of security for keeping information secure
import ssl
import smtplib
import datetime as dt
from emailFunction import send_email


load_dotenv()  # this reads the .env file

openai.api_key = os.getenv('API_KEY')

prompt = "Tell mommy how much I love her"
completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
)

body = completion.choices[0].message

print(body.content.strip())

send_email(body.content.strip())
