import email
from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv() # <-- Cargamos las variables 

app = FastAPI()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("EMAIL"), # <-- Cargamos las variables de Email y Password 
    MAIL_PASSWORD=os.getenv("PASSWORD"),
    MAIL_FROM=os.getenv("EMAIL"),
    MAIL_PORT=465,  #<--Pueto que usa GMAIL para enviar emails
    MAIL_SERVER="smtp.gmail.com", # <-- Servidor de GMAIl
    MAIL_STARTTLS=True, # <-- activamos el cifrado del email
    MAIL_SSL_TLS=False
)

# <-- Manejo de CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Contacto(BaseModel):
    nombre: str
    email: str
    mensaje: str 

@app.post("/contacto")
async def contacto(data: Contacto):
    message = MessageSchema(
        subject=f" Nuevo mensaje de {data.nombre}",
        recipients=[os.getenv("EMAIL")],
        body=f"Nombre{data.nombre}\nEmail: {data.email} \nMensaje: {data.mensaje}",
        subtype="plain" # <-- Formato de texto simple
    )
    fm = FastMail(conf)  # <-- Crear el objeto que usa la configuración de Gmail
    await fm.send_message(message) # <-- Envia el email y espera a que termine 
   
    return { "message": "Recibido"}