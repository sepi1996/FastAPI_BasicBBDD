from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


from models import homework as homework, user as user

from bbdd.database import engine

##Esto nos sirve para crear los modelos en la BBDD
user.SQLModel.metadata.create_all(bind=engine)
homework.SQLModel.metadata.create_all(bind=engine)


from router.user_router import router as user_router
from router.homework_router import router as homework_router

app = FastAPI()


app.include_router(user_router)
app.include_router(homework_router)

