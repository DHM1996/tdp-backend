from schema.works import NewWorkSchema, UpdateWorkSchema
from validator.validator import validate_work, validate_appointment, validate_work_update
from db.dao import works as works_dao


def create_work(work: NewWorkSchema):
    validate_work(work)
    works_dao.create_work(work)
    return {"message": "The work has been created successfully"}


def get_work_by_appointment_id(appointment_id):
    validate_appointment(appointment_id)
    return works_dao.get_work_by_appointment_id(appointment_id)


def update_work(work_update: UpdateWorkSchema):
    validate_work_update(work_update)
    works_dao.update_work(work_update)
    return {"message": "The work has been updated successfully"}
