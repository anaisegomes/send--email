import os
import smtplib
from email.message import EmailMessage

# configurar email, senha
EMAIL_ADRESS = "youremail"
EMAIL_PASSWORD = 'yourpassword'

# criar um e-mail:
msg = EmailMessage()
msg['Subject'] = 'messege here'
msg['From'] = 'youremail'
msg['To'] = 'anotheremail.com'

# CORREÇÃO: usar set_content em vez de set_charset
msg.set_content('your message here')

# CORREÇÃO: adicionar vírgula entre host e porta
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
