from sqlalchemy.orm import Session
import schemas
import models


def create_events(db: Session, event: schemas.EventCreate):
    db_item = models.Events(user_id = event.user_id,
                            name = event.name,
                            data = event.date,
                            location = event.location)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_event(db: Session, event_id: int):
    return db.query(models.Events).filter(models.Events.id == event_id).first()

def get_events(db: Session,  skip: int = 0, limit: int = 10):
    return db.query(models.Users).offset(skip).limit(limit).all()

def delete_events(db: Session, event_id: int):
    db_item = db.query(models.Events).filter(models.Events.id == event_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return {"msg": "Event deleted Sucessfully"}
    else:
        return {"msg": "Event not found"}

def update_events(db: Session, event_id: int, event: schemas.UserUpdate):
    db_item = db.query(models.Events).filter(models.Events.id == event_id)
    if db_item:
        update_data = event.dict(exclude_unset=True)

        for key, values in update_data.items():
            setattr(update_data, key, values)

        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return {"msg": "Event not found"}