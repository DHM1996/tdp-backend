from pydantic import BaseModel
from pydantic.datetime_parse import datetime


class NewAppointmentSchema(BaseModel):
    user_id: int
    professional_id: int
    date: datetime


class UpdateAppointmentSchema(BaseModel):
    appointment_id: int
    date: datetime
    active: bool
