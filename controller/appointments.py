from schema.appointments import NewAppointmentSchema, UpdateAppointmentSchema
from validator.validator import validate_new_appointment, validate_appointment_update, validate_user
import db.dao.appointments as appointments_dao


def create_appointment(appointment: NewAppointmentSchema):
    validate_new_appointment(appointment)
    appointments_dao.create_appointment(appointment)
    return {"message": "The appointment was created successfully"}


def update_appointment(appointment_update: UpdateAppointmentSchema):
    validate_appointment_update(appointment_update)
    appointments_dao.update_appointment(appointment_update)
    return {"message": "The appointment was updated successfully"}


def get_user_appointments(user_id):
    validate_user(user_id)
    return appointments_dao.get_user_appointments(user_id)


def get_professional_appointments(professional_id):
    validate_user(professional_id)
    return appointments_dao.get_professional_appointments(professional_id)
