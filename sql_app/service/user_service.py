from typing import List
from sqlalchemy.orm import Session
from models.user import UserModel
from schema.user_schema import *
from utils.helper import get_hashed_password
from service.base import BaseService, BaseDataManager
from schema.user_schema import *

class UserDataManager(BaseDataManager):
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int) -> UserSchema:
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def get_user_by_email(self, email: str) -> UserSchema:
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def get_users(self, skip: int = 0, limit: int = 100) -> List[UserSchema]:
        return self.db.query(UserModel).offset(skip).limit(limit).all()
    

    def create_user(self, user: UserCreateSchema) -> UserSchema:
        hashed_password = get_hashed_password(plain_text_password=user.password)
        db_user = UserModel(email=user.email, hashed_password=hashed_password)
        #self.add_one(db_user)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        ##Con esto podemos ver que nos aportan las funciones que añadimos en el base model
        print(db_user.to_dict())
        print(db_user.table_name())
        return db_user
    
    def delete_userv1(self, user_id: int) -> None:
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()

class UserService(BaseService):

    def get_user(self, user_id: int) -> UserSchema:
        return UserDataManager(self.session).get_user(user_id)

    def get_user_by_email(self, email: str) -> UserSchema:
        return UserDataManager(self.session).get_user_by_email(email)

    def get_users(self, skip: int = 0, limit: int = 100) -> List[UserSchema]:
        return UserDataManager(self.session).get_users(skip, limit)
    

    def create_user(self, user: UserCreateSchema) -> UserSchema:
        return UserDataManager(self.session).create_user(user)

    def delete_userv1(self, user_id: int) -> None:
        UserDataManager(self.session).delete_userv1(user_id)

    def delete_userv2(self, user_id: int) -> None:
        UserDataManager(self.session).delete_userv1(user_id)