from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema.user import *
from config.db import get_db, engine
from controller import accessController
from model import user
from model import turn

access = APIRouter()

user.Base.metadata.create_all(bind=engine)
turn.Base.metadata.create_all(bind=engine)

@access.post("/register/", status_code=200)
def register(user: UserLoginSchema, db: Session = Depends(get_db)):
    return accessController.register(user, db)

@access.post("/login/", status_code=200)
def login(user: UserLoginSchema, db: Session = Depends(get_db)):
    return accessController.login(user, db)