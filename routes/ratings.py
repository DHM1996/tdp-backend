from fastapi import APIRouter
from schema.ratings import RatingSchema
import controller.ratings as controller

rating_router = APIRouter()


@rating_router.post("/rating", status_code=200)
def create_rating(rating: RatingSchema):
    return controller.create_rating(rating)


@rating_router.get("/rating", status_code=200)
def get_ratings_by_professional_id(professional_id):
    return controller.get_ratings_by_professional_id(professional_id)
