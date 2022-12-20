from . import Base
from sqlalchemy import Column, Integer, String


class Profession(Base):
    __tablename__ = "professions"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    link_pic = Column(String)
