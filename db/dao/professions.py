from db import db_session
from db.model.professions import Profession


def get_profession_by_id(profession_id):
    return db_session.query(Profession.title).filter(Profession.id == profession_id).first()


def get_professions():
    return db_session.query(Profession).all()
