from pydantic import BaseModel


class AccessSchema(BaseModel):
    username: str
    password: str
