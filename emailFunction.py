import os
from email.message import EmailMessage
#layer of security for keeping information secure
import ssl
import smtplib
import datetime as dt
today = dt.datetime.today().strftime('%m/%d/%Y')

from dotenv import load_dotenv
load_dotenv()

def send_email(body):
    """Send introductory email"""
    email_sender="vincentypedro@gmail.com"
    email_password = os.environ.get("EMAIL_PASSWORD")
    email_receiver = "vincentypedro@gmail.com"

    

    em = EmailMessage()

    em['From'] = "Pedro Vincenty"
    em['To'] = email_receiver
    em['Subject'] = f"Email for Mommy {today}"

    em.set_content(body)
        
    
    context = ssl.create_default_context()


    try:
        #from stack overflow
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.send_message(em)
            return "Sent!"
    except:
        return "error sending email"
    

    