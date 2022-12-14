from schema.user import *
from sqlalchemy.orm import Session
from config.user import *
from schema.user import *
from fastapi import HTTPException

def update_profile(profile: UserProfileSchema, db: Session):
    user_db = get_user(profile.username, db)

    if user_db is None:
        raise HTTPException(status_code=401, detail="User not exist.")

    profile = profile.dict(exclude_unset=True, exclude_none=True, exclude={'email'})
    update_user(user_db, profile, db)
    
    return "Profile updated successfully."

def get_profile(username: str, db: Session):
    user_db = get_user(username, db)

    if user_db is None:
        raise HTTPException(status_code=400, detail="User not exist.")

    return user_db

def fetch_professionals(features: Features, db: Session):
    return get_professionals_by_features(features, db)