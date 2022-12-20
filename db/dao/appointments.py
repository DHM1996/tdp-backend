from db import db_session
from db.model.appointments import Appointment
from schema.appointments import NewAppointmentSchema, UpdateAppointmentSchema


def create_appointment(appointment: NewAppointmentSchema):
    try:
        db_appointment = Appointment(user_id=appointment.user_id,
                                     professional_id=appointment.professional_id,
                                     date=appointment.date,
                                     active=True)
        db_session.add(db_appointment)
        db_session.commit()
        db_session.refresh(db_appointment)
    except Exception as err:
        db_session.rollback()


def get_appointment(appointment_id):
    try:
        appointment = db_session.query(Appointment).filter(Appointment.id == appointment_id).first()
        return appointment
    except Exception as err:
        db_session.rollback()


def update_appointment(appointment_update: UpdateAppointmentSchema):
    try:
        db_session.query(Appointment).filter(Appointment.id == appointment_update.appointment_id).update(
            {
                Appointment.date: appointment_update.date,
                Appointment.active: appointment_update.active
            }
        )
        db_session.commit()
    except Exception as err:
        db_session.rollback()


def get_user_appointments(user_id):
    try:
        return db_session.query(Appointment).filter(Appointment.user_id == user_id).all()
    except Exception as err:
        db_session.rollback()


def get_professional_appointments(professional_id):
    try:
        return db_session.query(Appointment).filter(Appointment.professional_id == professional_id).all()
    except Exception as err:
        db_session.rollback()
