from sqlalchemy import func

from db import db_session
from db.model.users import User


def get_professionals_by_profession(profession_id):
    try:
        query = db_session.query(User.id, User.name, User.link_pic, User.longitude, User.latitude, User.profession_id)

        if profession_id:
            query = query.filter(User.profession_id == profession_id)
        else:
            query = query.filter(User.profession_id != None)
        return query.all()

    except Exception as err:
        db_session.rollback()


def get_professional_by_id(professional_id):
    try:
        return db_session.query(User.id, User.name, User.link_pic, User.longitude, User.latitude, User.profession_id).filter(
            User.id == professional_id).filter(User.profession_id != None).all()
    except Exception as err:
        db_session.rollback()


def get_professional_by_name(professional_name, profession_id=None):
    try:
        query = db_session.query(User.id, User.name, User.link_pic, User.longitude, User.latitude, User.profession_id).filter(func.lower(User.name).like(f'%{professional_name.lower()}%'))
        if profession_id:
            query = query.filter(User.profession_id == profession_id)
        else:
            query = query.filter(User.profession_id != None)
        return query.all()
    except Exception as err:
        db_session.rollback()
