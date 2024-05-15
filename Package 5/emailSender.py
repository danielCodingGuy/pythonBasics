#Simple python app that will send emails.
#author: danielCodingGuy

import smtplib

#Our mail info.
sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "P@ss123"
subject = "Test Mail"
body = "Test email written with python."

#Header.
message = f""" 
From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

#Server stuff necessary for sending our messages.
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

#Basic exception handling.
try:
    server.login(sender, password)
    print("Logged in successfully.")
    server.sendmail(sender, receiver, message)
    print("Email has been sent.")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in.")