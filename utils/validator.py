from fastapi import HTTPException

from db.dao import \
    user as user_dao, \
    professions as professions_dao, \
    appointments as appointments_dao

from schema.appointments import NewAppointmentSchema, UpdateAppointmentSchema


def validate_user(user_id):
    db_user = user_dao.get_user_by_id(user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User does not exist")
    return db_user


def validate_profession(profession_id):
    profession = professions_dao.get_profession_by_id(profession_id)
    if not profession:
        raise HTTPException(status_code=400, detail="Invalid Profession")


def validate_appointment(appointment: NewAppointmentSchema):
    db_user = user_dao.get_user_by_id(appointment.user_id)

    if not db_user:
        raise HTTPException(status_code=400, detail="User id does not exist")

    db_professional = user_dao.get_user_by_id(appointment.professional_id)
    if not db_professional:
        raise HTTPException(status_code=400, detail="The professional id does not exist")

    if db_user.id == db_professional.id:
        raise HTTPException(status_code=400, detail="The user and the professional must be different users")

    if db_professional.profession_id is None:
        raise HTTPException(status_code=400, detail="The professional must have a profession assigned")


def validate_appointment_update(appointment_update: UpdateAppointmentSchema):
    db_appointment = appointments_dao.get_appointment(appointment_update.appointment_id)

    if not db_appointment:
        raise HTTPException(status_code=400, detail="Invalid appointment id")

    if not db_appointment.active:
        raise HTTPException(status_code=400, detail="The appointment was previously cancelled. No changes are allowed")

