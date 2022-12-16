from fastapi import APIRouter
import controller.professionals as controller

professional_router = APIRouter()


@professional_router.get("/professionals", status_code=200)
def get_professionals(professional_id=None,
                      profession_id=None,
                      user_longitude=None,
                      user_latitude=None,
                      dist=None):

    return controller.get_professionals(professional_id,
                                        profession_id,
                                        user_longitude,
                                        user_latitude,
                                        dist)
