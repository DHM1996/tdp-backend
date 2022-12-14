from . import Base
from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    name = Column(String)
    bio = Column(String)
    ocupation = Column(String)
    location = Column(String)
    professional = Column(Boolean)
    pic = Column(String)
