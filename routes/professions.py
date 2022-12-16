import controller.professions as controller
from fastapi import APIRouter

professions_router = APIRouter()


@professions_router.get("/professions", status_code=200)
def get_professions(profession_id=None):
    return controller.get_professions(profession_id)
