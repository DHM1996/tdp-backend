from db import db_session
from db.model.appointments import Appointment
from db.model.ratings import Rating
from db.model.works import Work
from schema.ratings import RatingSchema


def create_rating(rating: RatingSchema):
    db_rating = Rating(work_id=rating.work_id,
                       rating=rating.rating,
                       comments=rating.comments)
    db_session.add(db_rating)
    db_session.commit()
    db_session.refresh(db_rating)


def get_ratings_by_professional_id(professional_id):
    return db_session.query(Rating, Work, Appointment).join(Work, Rating.work_id == Work.id).join(
        Appointment, Work.appointment_id == Appointment.id).all()


def get_rating_by_work_id(work_id):
    return db_session.query(Rating).filter(Rating.work_id == work_id).first()
