from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

APP_PASSWORD = os.getenv("APP_PASSWORD")
FROM_EMAIL = os.getenv("FROM_EMAIL")

message = EmailMessage()

message["Subject"] = "Hello from Python!"
message["From"] = FROM_EMAIL
message["To"] = "bojnordiraha@gmail.com"

message.set_content("Greetings from Python")

photo = open("attachments/images/Free_IRAN.png", "rb").read()
message.add_attachment(photo, maintype="image", subtype="png")

print(message)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email_server:
    email_server.login(FROM_EMAIL, APP_PASSWORD)
    email_server.send_message(message)

print("Email3 was sent successfully!")