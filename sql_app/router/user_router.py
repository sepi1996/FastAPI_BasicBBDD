from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session

from bbdd.database import create_session

from service.user_service import UserService
from schema.user_schema import *


router = APIRouter(
    prefix="/api",
    tags=["user"]
)

@router.post('/users/', response_model=UserSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(create_session))  -> UserSchema:
    db_user = UserService(db).get_user_by_email(email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")

    return UserService(db).create_user(user=user)


@router.get('/users/', response_model=List[UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(create_session)) -> List[UserSchema]:
    users = UserService(db).get_users(skip=skip, limit=limit)

    return users


@router.get('/users/{user_id}', response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(create_session)) -> UserSchema:
    db_user = UserService(db).get_user(user_id=user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")

    return db_user

@router.post('/users/deletev1/', response_model=None)
def delete_user(user_deletion: UserDeletionSchema, db: Session = Depends(create_session)) -> None:
    UserService(db).delete_userv1(user_deletion.id)

#Este es un ejemplo de como no debe hacerse el delete
@router.get('/users/deletev2/{user_id}', response_model=None)
def delete_user(user_id: int, db: Session = Depends(create_session)) -> None:
    UserService(db).delete_userv2(user_id)