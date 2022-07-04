import jwt
from fastapi import (
    BackgroundTasks,
    UploadFile,
    File,
    Form,
    Depends,
    HTTPException,
    status,
)

from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import dotenv_values


from .schema import EmailSchema
from .models import UserModel

credentials = dotenv_values("../.env")

# config for email
config: ConnectionConfig = ConnectionConfig(
    MAIL_USERNAME=credentials["EMAIL"],
    MAIL_PASSWORD=credentials["EMAIL_PASSWORD"],
    MAIL_FROM=credentials["EMAIL"],
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
)


async def send_email(email: EmailSchema, instance: UserModel):
    token_data: dict = {
        "id": instance.id,
        "username": instance.username,
    }
    token = jwt.encode(token_data, credentials["SECRET"])
    
