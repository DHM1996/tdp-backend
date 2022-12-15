from schema.turn import *
from sqlalchemy.orm import Session
from config.user import *
from config.turn import *
from fastapi import HTTPException


def request_turn(turn: TurnSchema, db: Session):
    user_db = get_user_by_id(turn.user_id, db)
    professional_db = get_user_by_id(turn.professional_id, db)

    if (user_db is None) or (professional_db is None):
        raise HTTPException(status_code=401, detail="User not exist.")

    if professional_db.professional is False:
        raise HTTPException(status_code=401, detail="Permission denied.")

    create_turn(turn, db)

    return "OK"


def get_turns_by_user(user_id: int, db: Session):
    user_db = get_user_by_id(user_id, db)

    if user_db is None:
        raise HTTPException(status_code=401, detail="User not exist.")

    return get_turns_by_user_id(user_id, db)


def get_turns_by_professional(user_id: int, db: Session):
    user_db = get_user_by_id(user_id, db)

    if user_db is None:
        raise HTTPException(status_code=401, detail="User not exist.")

    return get_turns_by_professional_id(user_id, db)
