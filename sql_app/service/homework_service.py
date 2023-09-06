from typing import List
from sqlalchemy.orm import Session
from models.homework import HomeWorkModel
from utils.helper import get_hashed_password
from service.base import BaseService, BaseDataManager
from schema.homework_schema import *


class HomeWorkDataManager(BaseDataManager):
    def __init__(self, db: Session):
        self.db = db


    def get_home_works(self, skip: int = 0, limit: int = 100) -> List[HomeWorkSchema]:
        return self.db.query(HomeWorkModel).offset(skip).limit(limit).all()

    def create_user_home_work(self, homework: HomeWorkCreateSchema, owner_id) -> HomeWorkSchema:
        db_home_work = HomeWorkModel(**homework.dict(), owner_id=owner_id)
        self.db.add(db_home_work)
        self.db.commit()
        self.db.refresh(db_home_work)

        return db_home_work

class HomeWorkService(BaseService):
    #def __init__(self, db: Session):
        #self.db = db
        #self.data_manager = HomeWorkDataManager(db)

    def get_home_works(self, skip: int = 0, limit: int = 100) -> List[HomeWorkSchema]:
        return HomeWorkDataManager(self.session).get_home_works(skip, limit)

    def create_user_home_work(self, home_work: HomeWorkCreateSchema, owner_id : int) -> HomeWorkSchema:
        return HomeWorkDataManager(self.session).create_user_home_work(home_work, owner_id)

