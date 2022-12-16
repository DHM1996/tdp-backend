from . import Base
from sqlalchemy import Integer, String, Column, Boolean, ForeignKey


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    name = Column(String)
    surname = Column(String)
    link_pic = Column(String)
    longitude = Column(String)
    latitude = Column(String)
    profession = Column(Integer, ForeignKey("professions.id"))
