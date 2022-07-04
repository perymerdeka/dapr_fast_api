from fastapi.responses import JSONResponse
from fastapi import status

from .models import user_pydanticIn, UserModel, user_pydantic
from .authentication import get_hashed_password


async def register(user: user_pydanticIn) -> JSONResponse:
    user_info: dict = user.dict(exclude_unset=True)
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
