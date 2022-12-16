from db import db_session
from db.model.users import User


def get_professionals(profession_id):
    return db_session.query(User).filter(User.profession_id == profession_id).all()


def get_professional(professional_id):
    return db_session.query(User).filter(User.id == professional_id). \
        filter(User.profession_id != None).first()
