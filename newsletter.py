import os
from email.message import EmailMessage
#layer of security for keeping information secure
import ssl
import smtplib
import datetime as dt
today = dt.datetime.today().strftime('%m/%d/%Y')

##Save below for future when want to provide an attachment
from dotenv import load_dotenv
load_dotenv()

import random

pokemon = ["Blastoise", "Mewtwo", "Charizard", "Kabutops", "Onix", "Gengar"]


email_sender = "vincentypedro@gmail.com"
email_password = os.environ.get("EMAIL_PASSWORD")
email_receiver = "vincentypedro@gmail.com"

subject = f"Today\'s Email {today}"
body= f"Hello,\n\nHere's today's pokemon: {random.choice(pokemon)}\n\nBest,\nPedro"

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


#     # make sure you’re up to date
# git fetch origin

# # switch to main
# git checkout main

# # bring main up to date with remote
# git pull origin main

# # merge your feature/work branch into main
# git merge your-branch-name

# # push updated main back to remote
# git push origin main

# # delete your local branch
# git branch -d your-branch-name

# # (optional) delete branch from remote too
# git push origin --delete your-branch-name