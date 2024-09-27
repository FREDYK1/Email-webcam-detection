import os
import glob
import smtplib
import mimetypes
from email.message import EmailMessage
import time

PASSWORD = "vtse cxha iaxe odwh"
SENDER = "frederickkankam7@gmail.com"
RECEIVER = "frederickkankam7@gmail.com"

def send_email(image):
    email_message = EmailMessage()
    email_message["Subject"] = "A New Customer Has Arrived"
    email_message["From"] = SENDER
    email_message["To"] = RECEIVER
    email_message.set_content("A new customer has arrived. Please check the attached image.")

    with open(image, "rb") as file:
        content = file.read()

    mime_type, _ = mimetypes.guess_type(image)
    main_type, sub_type = mime_type.split('/')

    email_message.add_attachment(content, maintype=main_type, subtype=sub_type)

    for attempt in range(3):  # Retry up to 3 times
        try:
            gmail = smtplib.SMTP("smtp.gmail.com", 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login(SENDER, PASSWORD)
            gmail.send_message(email_message)
            gmail.quit()
            print("Email sent successfully")
            break
        except smtplib.SMTPConnectError as e:
            print(f"Attempt {attempt + 1}: Failed to connect to the SMTP server: {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def delete_images():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)
