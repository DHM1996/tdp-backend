from fastapi import HTTPException

from db.dao import \
    user as user_dao, \
    professions as professions_dao, \
    appointments as appointments_dao, \
    works as works_dao,\
    ratings as ratings_dao

from db.model.appointments import Appointment
from db.model.users import User
from db.model.works import Work

from schema.appointments import NewAppointmentSchema, UpdateAppointmentSchema
from schema.ratings import RatingSchema
from schema.works import NewWorkSchema, UpdateWorkSchema


def validate_user(user_id):
    db_user: User = user_dao.get_user_by_id(user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User does not exist")
    return db_user


def validate_profession(profession_id):
    profession = professions_dao.get_profession_by_id(profession_id)
    if not profession:
        raise HTTPException(status_code=400, detail="Invalid Profession")


def validate_new_appointment(appointment: NewAppointmentSchema):
    db_user: User = user_dao.get_user_by_id(appointment.user_id)

    if not db_user:
        raise HTTPException(status_code=400, detail="User id does not exist")

    db_professional: User = user_dao.get_user_by_id(appointment.professional_id)
    if not db_professional:
        raise HTTPException(status_code=400, detail="The professional id does not exist")

    if db_user.id == db_professional.id:
        raise HTTPException(status_code=400, detail="The user and the professional must be different users")

    if db_professional.profession_id is None:
        raise HTTPException(status_code=400, detail="The professional must have a profession assigned")


def validate_appointment_update(appointment_update: UpdateAppointmentSchema):
    db_appointment: Appointment = appointments_dao.get_appointment(appointment_update.appointment_id)

    if not db_appointment:
        raise HTTPException(status_code=400, detail="Invalid appointment id")

    if not db_appointment.active:
        raise HTTPException(status_code=400, detail="The appointment was previously cancelled. No changes are allowed")


def validate_appointment(appointment_id):
    db_appointment: Appointment = appointments_dao.get_appointment(appointment_id)
    if not db_appointment:
        raise HTTPException(status_code=400, detail="The appointment does not exists")
    if not db_appointment.active:
        raise HTTPException(status_code=400, detail="The appointment is canceled")


def validate_work(work: NewWorkSchema):
    validate_appointment(work.appointment_id)
    db_work: Work = works_dao.get_work_by_appointment_id(work.appointment_id)
    if db_work:
        raise HTTPException(status_code=400, detail="There is already a work associated with the appointment selected")


def validate_work_update(work_update: UpdateWorkSchema):
    db_work: Work = works_dao.get_work_by_work_id(work_update.work_id)
    if not db_work:
        raise HTTPException(status_code=400, detail="The work does not exist")
    if db_work.paid:
        raise HTTPException(status_code=400, detail="A paid work could not be updated")


def validate_rating(rating: RatingSchema):
    db_work = works_dao.get_work_by_work_id(rating.work_id)
    if not db_work:
        raise HTTPException(status_code=400, detail="The work does not exist")
    db_rating = ratings_dao.get_rating_by_work_id(rating.work_id)
    if db_rating:
        raise HTTPException(status_code=400, detail="A rating is already created for this work")
    if rating.rating < 0 or rating.rating > 5:
        raise HTTPException(status_code=400, detail="The raiting must be between 0 and 5")
