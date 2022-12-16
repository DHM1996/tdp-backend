from . import Base
from sqlalchemy import Column, String, Integer, Numeric, Boolean, ForeignKey


class Work(Base):
    __tablename__ = "works"
    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"))
    title = Column(String)
    description = Column(String)
    price = Column(Numeric)
    paid = Column(Boolean)




