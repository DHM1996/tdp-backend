from . import Base
from sqlalchemy import Integer, Column, Date


class Turn(Base):
    __tablename__ = "turns"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    professional_id = Column(Integer)
    day = Column(Date)
    price = Column(Integer)
