from fastapi import HTTPException, status
import jwt
from passlib.context import CryptContext
from dotenv import dotenv_values

from .models import UserModel

pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

credentials: dict = dotenv_values("../.env")

def get_hashed_password(password: str) -> str:
    return pwd_context.hash(password)

async def verify_token(token: str) -> UserModel:
    try:
        payload = jwt.decode(token, credentials['SECRET'], algorithms=["HS256"])
        user = await UserModel.get(id=payload.get("id"))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user