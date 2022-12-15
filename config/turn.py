from schema.turn import *
from model.turn import Turn
from sqlalchemy.orm import Session


def create_turn(turn: TurnSchema, db: Session):
    turn_db = Turn(user_id=turn.user_id, professional_id=turn.professional_id, day=turn.day, price=turn.price)
    db.add(turn_db)
    db.commit()
    db.refresh(turn_db)
    return turn_db


def get_turns_by_user_id(user_id: int, db: Session):
    return db.query(Turn).filter(Turn.user_id == user_id).all()


def get_turns_by_professional_id(user_id: int, db: Session):
    return db.query(Turn).filter(Turn.professional_id == user_id).all()
