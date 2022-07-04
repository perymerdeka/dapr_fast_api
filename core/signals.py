from tortoise.signals import post_save
from tortoise import BaseDBAsyncClient
from typing import Type, List, Optional

from .models import UserModel, bussiness_pydantic

@post_save(sender=UserModel)
async def create_bussiness(
    sender: "Type[UserModel]",
    instance: UserModel,
    created: bool,
    using_db: Optional[BaseDBAsyncClient],
    update_fields: List[str],
) -> None:
    if created:
        bussiness_objects: UserModel = await UserModel.create(
            bussiness_name = instance.username, owner_id = instance
        )
        await bussiness_pydantic.from_tortoise_orm(bussiness_objects)
        
        # send email
        