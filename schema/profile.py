from pydantic import BaseModel
from typing import Optional


class ProfileSchema(BaseModel):
    user_id: int
    name: str
    link_pic: str
    longitude: int
    latitude: int
    profession_id: Optional[int]
