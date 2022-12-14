from pydantic import BaseModel
from datetime import date

class TurnSchema(BaseModel):
    user_id: int
    professional_id: int
    day: date
    price: int