from pydantic import BaseModel


class ProfileSchema(BaseModel):
    user_id: int
    name: str
    surname: str
    link_pic: str
    longitude: str
    latitude: str
    profession_id: int
