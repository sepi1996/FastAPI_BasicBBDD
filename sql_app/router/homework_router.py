from typing import List

from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.orm import Session

from bbdd.database import create_session

from service.homework_service import HomeWorkService
from schema.homework_schema import *


router = APIRouter(
    prefix="/api",
    tags=["homework"]
)


@router.post('/users/{user_id}/home-works/', response_model=HomeWorkSchema)
def create_home_work_for_user(user_id: int, home_work: HomeWorkCreateSchema, db: Session = Depends(create_session)):
    return HomeWorkService(db).create_user_home_work(home_work=home_work, owner_id=user_id)


@router.get('/home-works/', response_model=List[HomeWorkSchema])
def read_home_works(skip: int = 0, limit: int = 100, db: Session = Depends(create_session)):
    home_works = HomeWorkService(db).get_home_works(skip=skip, limit=limit)

    return home_works


