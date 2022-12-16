from . import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    professional_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Integer)

