from fastapi import APIRouter
from schema.works import NewWorkSchema, UpdateWorkSchema
import controller.works as controller

work_router = APIRouter()


@work_router.post("/work", status_code=200)
def create_work(work: NewWorkSchema):
    return controller.create_work(work)


@work_router.get("/work", status_code=200)
def get_work(appointment_id):
    return controller.get_work_by_appointment_id(appointment_id)


@work_router.put("/work", status_code=200)
def update_work(work_update: UpdateWorkSchema):
    return controller.update_work(work_update)
