# Abstract Class: Schema

from pydantic import BaseModel
from typing import List

class EmailSchema(BaseModel):
    email: List[str]

