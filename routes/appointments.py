import controller.appointments as controller
from fastapi import APIRouter

from schema.appointments import NewAppointmentSchema, UpdateAppointmentSchema

appointments_router = APIRouter()


@appointments_router.post("/appointments/", status_code=200)
def register(appointment: NewAppointmentSchema):
    return controller.create_appointment(appointment)


@appointments_router.put("/appointments/", status_code=200)
def update_appointment(appointment_update: UpdateAppointmentSchema):
    return controller.update_appointment(appointment_update)


@appointments_router.get("/appointments/user", status_code=200)
def get_user_appointments(user_id):
    return controller.get_user_appointments(user_id)


@appointments_router.get("/appointments/professional", status_code=200)
def get_professional_appointments(professional_id):
    return controller.get_professional_appointments(professional_id)
