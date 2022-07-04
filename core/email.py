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

credentials = dotenv_values(".env")


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
    print(credentials)
    token_data: dict = {
        "id": instance.id,
        "username": instance.username,
    }
    token = jwt.encode(token_data, credentials["SECRET"], algorithm="HS256")
    template = f"""
        <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
            <div style=" display: flex; align-items: center; justify-content: center; flex-direction: column;">
                <h3> Account Verification </h3>
                <br>
                <p>Thanks for choosing EasyShopas, please 
                click on the link below to verify your account</p> 
                <a style="margin-top:1rem; padding: 1rem; border-radius: 0.5rem; font-size: 1rem; text-decoration: none; background: #0275d8; color: white;"
                 href="http://localhost:8000/verification/?token={token}">
                    Verify your email
                <a>
                <p style="margin-top:1rem;">If you did not register for EasyShopas, 
                please kindly ignore this email and nothing will happen. Thanks<p>
            </div>
        </body>
        </html>
    """
    message = MessageSchema(
        subject="EasyShopas Account Verification Mail",
        recipients=email,
        body=template,
        subtype="html"
        )

    fm = FastMail(config)
    await fm.send_message(message) 
    
