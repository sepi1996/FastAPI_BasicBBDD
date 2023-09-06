from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base import SQLModel



class HomeWorkModel(SQLModel):
    __tablename__ = 'home_works'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('UserModel', back_populates='home_works')