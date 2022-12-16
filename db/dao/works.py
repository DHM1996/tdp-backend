from db import db_session
from db.model.works import Work
from schema.works import NewWorkSchema, UpdateWorkSchema


def create_work(work: NewWorkSchema):
    db_work = Work(appointment_id=work.appointment_id,
                   title=work.title,
                   description=work.description,
                   price=work.price,
                   paid=False)
    db_session.add(db_work)
    db_session.commit()
    db_session.refresh(db_work)


def get_work_by_appointment_id(appointment_id):
    return db_session.query(Work).filter(Work.appointment_id == appointment_id).first()


def get_work_by_work_id(work_id):
    return db_session.query(Work).filter(Work.id == work_id).first()


def update_work(work_update: UpdateWorkSchema):
    db_session.query(Work).filter(Work.id == work_update.work_id).update(
        {
            Work.title: work_update.title,
            Work.description: work_update.description,
            Work.price: work_update.price,
            Work.paid: work_update.paid
        }
    )
    db_session.commit()
