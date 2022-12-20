from schema.ratings import RatingSchema, GetRatingSchema
from validator.validator import validate_rating, validate_user
import db.dao.ratings as ratings_dao


def create_rating(rating: RatingSchema):
    validate_rating(rating)
    ratings_dao.create_rating(rating)
    return {"message": "the rating was created successfully"}


def get_ratings_by_professional_id(professional_id):
    validate_user(professional_id)
    result = ratings_dao.get_ratings_by_professional_id(professional_id)
    ratings = []
    total = 0
    for rating in result:
        ratings.append(
            GetRatingSchema(
                user_id=rating["Appointment"].user_id,
                professional_id=rating["Appointment"].professional_id,
                rating=rating["Rating"].rating,
                comments=rating["Rating"].comments
            )
        )
        total += rating["Rating"].rating

    cant = len(ratings)

    if cant != 0:
        mean = total / len(ratings)

    else:
        mean = 0

    return {
        "ratings": ratings,
        "mean": mean
    }
