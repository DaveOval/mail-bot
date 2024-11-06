from email.message import EmailMessage
import ssl
import smtplib
import imaplib

email_reciever = "dave_u@outlook.com"

lista_de_correos = ["jose-esteva@hybridge.com"]

asunto = "Mira esta notificacion"

cuerpo = '''
   Hola que pedo 
'''

def contestar_correos(mensaje):
    pass


def enviar_correo( mensaje , asunto , destinatarios ):
    email_sender = "mailbotj@gmail.com"
    email_sender_password = "lgizhcbskstvgjjj"
    email = EmailMessage()

    email["From"] = email_sender

    email["To"] = ",".join(destinatarios)

    email["Subject"] = cuerpo

    email.set_content( mensaje )

    contexto = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", context=contexto) as smtp:
        smtp.login(email_sender, email_sender_password)
        smtp.sendmail(email_sender, destinatarios, email.as_string())


enviar_correo(cuerpo, asunto, lista_de_correos)
