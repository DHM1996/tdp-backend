from schema.user import *
from fastapi import HTTPException
from sqlalchemy.orm import Session
from config.user import get_user, create_user


def register(user: UserLoginSchema, db: Session):
    user_db = get_user(user.username, db)

    if user_db is not None:
        raise HTTPException(status_code=401, detail="User already exist.")

    return create_user(user, db)


def login(user: UserLoginSchema, db: Session):
    user_db = get_user(user.username, db)

    if user_db is None or user.password != user_db.password:
        raise HTTPException(status_code=401, detail="Username or password incorrect.")

    return "OK"
