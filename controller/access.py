from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from db.dao import user as user_dao
from db.model.users import User
from schema.access import AccessSchema


def register(user: AccessSchema):
    try:
        user_id = user_dao.create_user(user)

    except IntegrityError:
        raise HTTPException(status_code=401, detail="User already exist.")

    return {"user_id": user_id}


def login(user: AccessSchema):
    db_user: User = user_dao.get_user_by_username(user.username)

    if db_user is None or user.password != db_user.password:
        raise HTTPException(status_code=401, detail="Username or password incorrect.")

    return {"user_id": db_user.id}
