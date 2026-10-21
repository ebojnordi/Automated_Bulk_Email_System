from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

APP_PASSWORD = os.getenv("APP_PASSWORD")
FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")
#-------------------------------------------

# List of cntacts
contacts = [{
    "name": "Tina",
    "email": "tina@gmail.com",
    "project": "Project 1",
    "report": "attachments/PDFs/Report1.pdf",
    "known_issue": "The number of bugs in the system is increasing day by day. We need to address this issue immediately."},
    {
    "name": "Daniel",
    "email": "Daniel@gmail.com",
    "project": "Project 2",
    "report": "attachments/PDFs/Report2.pdf",
    "known_issue": "Performance issues with the latest update."}]
# ------------------------------------------

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email_server:
    email_server.login(FROM_EMAIL, APP_PASSWORD)

    for contact in contacts:
        message = EmailMessage()

        message["Subject"] = contact["project"] + " -- Status Update"
        message["From"] = FROM_EMAIL
        message["To"] = contact["email"]

        message.set_content(f"""
Hi {contact['name']},

This is a status update for the {contact['project']} project.

Known Issue: {contact['known_issue']}

Please find the attached report for more details.

Kind regards,
Ehsan
""")

        report_pdf = open(contact["report"], "rb").read()
        message.add_attachment(report_pdf, maintype="application", subtype="pdf", filename=contact["report"].split("/")[-1])
        email_server.send_message(message)

        print(f"Email to {contact['name']} was sent successfully!")