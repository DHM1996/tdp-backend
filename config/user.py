from schema.user import *
from model.user import User
from schema.user import *
from sqlalchemy.orm import Session


def create_user(user: UserLoginSchema, db: Session):
    user_db = User(username=user.username, password=user.password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db.id


def update_user(user_db: User, profile: dict(), db: Session):
    for attr, value in profile.items():
        setattr(user_db, attr, value)
    db.commit()
    db.refresh(user_db)
    return user_db


def get_user(username: str, db: Session):
    return db.query(User).filter(User.username == username).first()


def get_user_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def get_professionals_by_features(features: Features, db: Session):
    query = db.query(User).filter(User.professional == True)
    if features.username is not None:
        query = query.filter(User.username == features.username)
    if features.name is not None:
        query = query.filter(User.name == features.name)
    if features.ocupation is not None:
        query = query.filter(User.ocupation == features.ocupation)
    if features.location is not None:
        query = query.filter(User.location == features.location)
    return query.all()
