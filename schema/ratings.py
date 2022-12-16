from pydantic import BaseModel


class RatingSchema(BaseModel):
    work_id: int
    rating: int
    comments: str


class GetRatingSchema(BaseModel):
    user_id: int
    professional_id: int
    rating: str
    comments: str
