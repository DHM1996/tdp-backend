import db.dao.user as dao
from fastapi import HTTPException

from schema.user import LoginSchema


def register(user: LoginSchema):
    previous_user = dao.get_user(user.username)

    if previous_user is not None:
        raise HTTPException(status_code=401, detail="User already exist.")

    return dao.create_user(user)


def login(user: LoginSchema):
    db_user = dao.get_user(user.username)

    if db_user is None or user.password != db_user.password:
        raise HTTPException(status_code=401, detail="Username or password incorrect.")

    return "OK"
