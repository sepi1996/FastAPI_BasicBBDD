from typing import List, Optional
from pydantic import BaseModel


class HomeWorkBaseSchema(BaseModel):
    title: str
    description: Optional[str] = "-"

class HomeWorkCreateSchema(HomeWorkBaseSchema):
    pass


class HomeWorkSchema(HomeWorkBaseSchema):
    id: int
    owner_id: int

    class Config:
        orm_mode = True