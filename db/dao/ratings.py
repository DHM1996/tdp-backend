from db import db_session
from db.model.appointments import Appointment
from db.model.ratings import Rating
from db.model.works import Work
from schema.ratings import RatingSchema


def create_rating(rating: RatingSchema):
    try:
        db_rating = Rating(work_id=rating.work_id,
                           rating=rating.rating,
                           comments=rating.comments)
        db_session.add(db_rating)
        db_session.commit()
        db_session.refresh(db_rating)

    except Exception as err:
        db_session.rollback()


def get_ratings_by_professional_id(professional_id):
    try:
        return db_session.query(Rating, Work, Appointment).join(Work, Rating.work_id == Work.id).join(
            Appointment, Work.appointment_id == Appointment.id).filter(Appointment.professional_id == professional_id).all()

    except Exception as err:
        db_session.rollback()


def get_rating_by_work_id(work_id):
    try:
        return db_session.query(Rating).filter(Rating.work_id == work_id).first()

    except Exception as err:
        db_session.rollback()
