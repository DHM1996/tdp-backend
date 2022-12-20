from pydantic import BaseModel
from typing import Optional


class ProfileSchema(BaseModel):
    user_id: int
    name: Optional[str]
    link_pic: Optional[str]
    longitude: Optional[float]
    latitude: Optional[float]
    profession_id: Optional[int]
