from typing import List
from pydantic import BaseModel

from schema.homework_schema import HomeWorkSchema

class UserBaseSchema(BaseModel):
    email: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: int
    is_active: bool
    home_works: List[HomeWorkSchema] = []

    class Config:
        orm_mode = True #Esto nos sirve para acceder a los elementos de esta formna data.id y no con data["id"]


class UserDeletionSchema(BaseModel):
    id: int