from . import Base
from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, Numeric


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String)
    link_pic = Column(String)
    longitude = Column(Numeric)
    latitude = Column(Numeric)
    profession_id = Column(Integer, ForeignKey("professions.id"))
