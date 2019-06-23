import smtplib
import imghdr
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Hello there, This is test mail'
msg.set_content('Hello buddy this is test body')
msg['From'] = 'Enter your Email ID'
msg['To'] = 'Enter To Email ID'

with open('bg.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=f.name)

with smtplib.SMTP_SSL('smtp.gmail.com', '465') as smtp:
    smtp.login('Enter your email ID', 'Enter your password')

    smtp.send_message(msg)