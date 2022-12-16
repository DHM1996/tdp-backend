from fastapi import APIRouter

import controller.profile as controller
from schema.profile import ProfileSchema

profile_router = APIRouter()


@profile_router.get("/profile/", status_code=200, response_model=ProfileSchema)
def get_profile(user_id):
    result = controller.get_profile(user_id)
    return result


@profile_router.put("/profile/", status_code=200)
def update_profile(profile: ProfileSchema):
    return controller.update_profile(profile)
