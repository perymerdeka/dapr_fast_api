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

config_credentials = dotenv_values("../.env")

# config for email
config: ConnectionConfig = ConnectionConfig(
    MAIL_USERNAME="",
    MAIL_PASSWORD="",
    MAIL_FROM="",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
)

