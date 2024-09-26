import os
import glob
import smtplib
import imghdr
from email.message import EmailMessage


PASSWORD = "vtse cxha iaxe odwh"
SENDER = "frederickkankam7@gmail.com"
RECEIVER = "frederickkankam7@gmail.com"


def send_email(image):
    email_message = EmailMessage()
    email_message["Subject"] ="A New Customer Has Arrived"
    email_message.set_content("A new customer has arrived. "
                              "Please check the attached image.")

    with open(image, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image",
                                 subtype=imghdr.what(None, content))

    gmail =smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.send_message(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()


def delete_images():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)