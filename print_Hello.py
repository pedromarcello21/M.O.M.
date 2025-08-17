import os
from dotenv import load_dotenv

from email.message import EmailMessage
#layer of security for keeping information secure
import ssl
import smtplib

load_dotenv()

email_sender = "vincentypedro@gmail.com"
email_password = os.environ.get("EMAIL_PASSWORD")
email_receiver = "vincentypedro@gmail.com"

subject = "Flatiron Alumni Introduction | Pedro Vincenty"
body= f"Hello,\n\nI'm Pedro Vincenty, a fellow Flatiron Alum! I'd love to connect and learn more about the culture at ING.  \n\nIf you have any availability in the coming days, I'd love to schedule a 10 minute conversation.\n\nBest,\nPedro"

em = EmailMessage()

em['From'] = "Pedro Vincenty"
em['To'] = email_receiver
em['Subject'] = subject

em.set_content(body)

context = ssl.create_default_context()


try:
    #from stack overflow
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)
        print("Sent!")
except:
    print("error sending email")