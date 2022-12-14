from pydantic import BaseModel
from typing import Optional

class UserLoginSchema(BaseModel):
    username: str
    password: str

class UserProfileSchema(BaseModel):
    username: str
    name: str
    bio: Optional[str]
    ocupation: str
    location: str
    professional: bool
    pic: Optional[str]

class Features(BaseModel):
    username: Optional[str]
    name: Optional[str]
    ocupation: Optional[str]
    location: Optional[str]