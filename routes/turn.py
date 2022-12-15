from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.db import get_db, engine
from controller import turnController
from schema.turn import *
from model import turn

turn = APIRouter()


@turn.post("/request-turn/", status_code=200)
def request_turn(turn: TurnSchema, db: Session = Depends(get_db)):
    return turnController.request_turn(turn, db)


@turn.post("/get-turns-by-users/", status_code=200)
def get_turns_by_user(user_id: int, db: Session = Depends(get_db)):
    return turnController.get_turns_by_user(user_id, db)


@turn.post("/get-turns-by-professional/", status_code=200)
def get_turns_by_professional(user_id: int, db: Session = Depends(get_db)):
    return turnController.get_turns_by_professional(user_id, db)
