from fastapi import APIRouter


from schema.access import AccessSchema
import controller.access as controller

access_router = APIRouter()


@access_router.post("/register/", status_code=200)
def register(user: AccessSchema):
    return controller.register(user)


@access_router.post("/login/", status_code=200)
def login(user: AccessSchema):
    return controller.login(user)

