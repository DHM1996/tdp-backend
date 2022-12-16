from . import Base
from sqlalchemy import Integer, String, Column, Boolean, ForeignKey


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String)
    surname = Column(String)
    link_pic = Column(String)
    longitude = Column(String)
    latitude = Column(String)
    profession_id = Column(Integer, ForeignKey("professions.py.id"))
