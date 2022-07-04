from tortoise import Model, fields
from tortoise.contrib.pydantic import pydantic_model_creator

class UserModel(Model):
    id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=50, unique=True, null=False)
    email = fields.CharField(max_length=200, unique=True, null=False)
    password = fields.CharField(max_length=100, null=False)
    is_verified = fields.BooleanField(default=False)
    join_data = fields.DatetimeField(auto_now_add=True)
    
class BussinessModel(Model):
    id = fields.IntField(pk=True, index=True)
    bussiness_name = fields.CharField(max_length=50, unique=True, null=False)
    city = fields.CharField(max_length=100, null=False, default="Unspecified")
    region = fields.CharField(max_length=100, null=False, default="Unspecified")
    bussiness_description = fields.TextField(null=True)
    logo = fields.CharField(max_length=200, null=False, default="default.jpg")
    owner = fields.ForeignKeyField('models.UserModel', related_name='bussiness', on_delete=fields.CASCADE)
    
class ProductModel(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=50, null=False, index=True)
    category = fields.CharField(max_length=50, null=False, index=True)
    original_price = fields.DecimalField(max_digits=12, decimal_places=2)
    new_price = fields.DecimalField(max_digits=12, decimal_places=2)
    percentage_discount = fields.IntField()
    offer_expiration_date = fields.DatetimeField(null=True)
    product_image = fields.CharField(max_length=200, null=False, default="ProductDefault.jpg")
    bussiness = fields.ForeignKeyField('models.BussinessModel', related_name='products', on_delete=fields.CASCADE)
    
# pydantic models config
user_pydantic = pydantic_model_creator(UserModel, name="User", exclude=("is_verified", ))
user_pydanticIn = pydantic_model_creator(UserModel, name="UserIn", exclude_readonly=True, exclude=("is_verified", ))
user_pydanticOut = pydantic_model_creator(UserModel, name="UserOut", exclude=("password", ))

bussiness_pydantic = pydantic_model_creator(BussinessModel, name="Bussiness")
bussiness_pydanticIn = pydantic_model_creator(BussinessModel, name="BussinessIn", exclude_readonly=True)

product_pydantic = pydantic_model_creator(ProductModel, name="Product")
product_pydanticIn = pydantic_model_creator(ProductModel, name="ProductIn", exclude=("percentage_discount", "id",))

