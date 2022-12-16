from db import db_session
from db.model.appointments import Appointment
from schema.appointments import NewAppointmentSchema, UpdateAppointmentSchema


def create_appointment(appointment: NewAppointmentSchema):
    appointment_db = Appointment(user_id=appointment.user_id,
                                 professional_id=appointment.professional_id,
                                 date=appointment.date,
                                 active=True)
    db_session.add(appointment_db)
    db_session.commit()
    db_session.refresh(appointment_db)


def get_appointment(appointment_id):
    appointment = db_session.query(Appointment).filter(Appointment.id == appointment_id).first()
    return appointment


def update_appointment(appointment_update: UpdateAppointmentSchema):
    db_session.query(Appointment).filter(Appointment.id == appointment_update.appointment_id).update(
        {
            Appointment.date: appointment_update.date,
            Appointment.active: appointment_update.active
        }
    )
    db_session.commit()


def get_user_appointments(user_id):
    return db_session.query(Appointment).filter(Appointment.user_id == user_id).all()


def get_professional_appointments(professional_id):
    return db_session.query(Appointment).filter(Appointment.professional_id == professional_id).all()
