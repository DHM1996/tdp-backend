from db import db_session
from db.model.professions import Profession


def get_profession_by_id(profession_id):
    try:
        return db_session.query(Profession.title).filter(Profession.id == profession_id).first()
    except Exception as err:
        db_session.rollback()
        raise err


def get_professions():
    try:
        return db_session.query(Profession).all()
    except Exception as err:
        db_session.rollback()
        raise err
