from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.requests import Request
from fastapi import HTTPException, status
from fastapi.templating import Jinja2Templates

from .models import user_pydanticIn, UserModel, user_pydantic
from .authentication import get_hashed_password, verify_token

# configuring templates

templates = Jinja2Templates(directory="templates")

async def register(user: user_pydanticIn):
    user_info = user.dict(exclude_unset=True)
    user_info["password"] = get_hashed_password(user_info["password"])

    # create user
    user_object: UserModel = await UserModel.create(**user_info)
    new_user = await user_pydantic.from_tortoise_orm(user_object)
    return JSONResponse(
        {
            "status": status.HTTP_200_OK,
            "message": f"User {new_user.username} created successfully, please check your email.",
        },
        media_type="application/json",
    )


async def email_verification(request: Request, token: str) -> HTMLResponse:
    user: UserModel = await verify_token(token)
    if user and not user.is_verified:
        user.is_verified = True
        await user.save()
        return templates.TemplateResponse("verification.html", {"request": request, "user": user.username})
    
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )    