from email.message import EmailMessage
import ssl
import smtplib

email_sender = "mailbotj@gmail.com"
email_sender_password = "lgizhcbskstvgjjj"
email_reciever = "dave_u@outlook.com"

asunto = "Mira esta notificacion"

cuerpo = '''
   Hola que pedo 
'''

email = EmailMessage()

email["From"] = email_sender

email["To"] = email_reciever

email["Subject"] = cuerpo

email.set_content(cuerpo)

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", context = contexto) as smtp:
    smtp.login( email_sender, email_sender_password )
    smtp.sendmail(email_sender, email_reciever, email.as_string())