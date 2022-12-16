from sqlalchemy.exc import IntegrityError

from db import db_session
from db.model.users import User
from schema.access import AccessSchema
from schema.profile import ProfileSchema


def get_user_by_username(username: str):
    return db_session.query(User).filter(User.username == username).first()


def get_user_by_id(user_id: int):
    return db_session.query(User).filter(User.id == user_id).first()


def create_user(user: AccessSchema):
    try:
        user_db = User(username=user.username, password=user.password)
        db_session.add(user_db)
        db_session.commit()
        db_session.refresh(user_db)

    except IntegrityError as err:
        db_session.rollback()
        raise err

    return user_db.id


def update_profile(profile: ProfileSchema):
    db_session.query(User).filter(User.id == profile.user_id).update(
        {
            User.name: profile.name,
            User.surname: profile.surname,
            User.link_pic: profile.link_pic,
            User.longitude: profile.longitude,
            User.latitude: profile.latitude,
            User.profession_id: profile.profession_id
        }
    )
    db_session.commit()
