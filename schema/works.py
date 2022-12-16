from pydantic import BaseModel


class NewWorkSchema(BaseModel):
    appointment_id: int
    title: str
    description: str
    price: float
    paid: bool


class UpdateWorkSchema(BaseModel):
    work_id: int
    title: str
    description: str
    price: float
    paid: bool
