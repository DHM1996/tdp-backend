from db import db_session
from db.model.users import User
from schema.user import LoginSchema


def get_user(username: str):
    return db_session.query(User).filter(User.username == username).first()


def create_user(user: LoginSchema):
    user_db = User(username=user.username, password=user.password)
    db_session.add(user_db)
    db_session.commit()
    db_session.refresh(user_db)
    return user_db.id
