from . import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey


class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    professional_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime)
    active = Column(Boolean)

