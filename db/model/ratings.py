from . import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    work_id = Column(Integer, ForeignKey("works.id"))
    rating = Column(Integer)
    comments = Column(String)

