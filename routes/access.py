from fastapi import APIRouter, Depends
import controller.access as controller

from sqlalchemy.orm import Session

from schema.user import LoginSchema

access = APIRouter()


@access.post("/register/", status_code=200)
def register(user: LoginSchema):
    return controller.register(user)


@access.post("/login/", status_code=200)
def login(user: LoginSchema):
    return controller.login(user)
