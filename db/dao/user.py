from sqlalchemy.exc import IntegrityError

from db import db_session
from db.model.users import User
from schema.access import AccessSchema
from schema.profile import ProfileSchema


def get_user_by_username(username: str):
    try:
        return db_session.query(User).filter(User.username == username).first()

    except Exception as err:
        db_session.rollback()


def get_user_by_id(user_id: int):
    try:
        return db_session.query(User).filter(User.id == user_id).first()

    except Exception as err:
        db_session.rollback()


def create_user(user: AccessSchema):
    try:
        db_user = User(username=user.username, password=user.password)
        db_session.add(db_user)
        db_session.commit()
        db_session.refresh(db_user)
        return db_user.id

    except Exception as err:
        db_session.rollback()


def update_profile(profile: ProfileSchema):
    try:
        db_session.query(User).filter(User.id == profile.user_id).update(
            {
                User.name: profile.name,
                User.link_pic: profile.link_pic,
                User.longitude: profile.longitude,
                User.latitude: profile.latitude,
                User.profession_id: profile.profession_id
            }
        )
        db_session.commit()

    except Exception as err:
        db_session.rollback()
