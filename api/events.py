# from sqlalchemy.orm import Session
# import schemas
# import models
#
#
# def create_events(db: Session, items: schemas.EventCreate):
#     db_item = models.Events(user_id = items.user_id,
#                             name = items.name,
#                             data = items.date,
#                             location = items.location)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
#
# def get_event(db: Session, )