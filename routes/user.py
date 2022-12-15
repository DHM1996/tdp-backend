from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema.user import *
from config.db import get_db, engine
from controller import userController

user = APIRouter()


@user.post("/update-profile/", status_code=200)
def update_profile(profile: UserProfileSchema, db: Session = Depends(get_db)):
    return userController.update_profile(profile, db)


@user.post("/get-profile", status_code=200)
def get_profile(username: str, db: Session = Depends(get_db)):
    return userController.get_profile(username, db)


@user.post("/get-professionals-by-features/", status_code=200)
def get_professionals(features: Features, db: Session = Depends(get_db)):
    return userController.fetch_professionals(features, db)
