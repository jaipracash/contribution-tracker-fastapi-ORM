from sqlalchemy.orm import Session
import schemas
import models

def create_contributions(db: Session, contribution: schemas.ContributionCreate):
    db_item = models.Contribuitons(event_id = contribution.event_id, name = contribution.name, address = contribution.address, amount = contribution.amount, mobile_number = contribution.mobile_number)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_contribution(db: Session, contribution_id = int):
    return db.query(models.Contribuitons).filter(models.Contribuitons.id == contribution_id).first()

def get_contributions(db: Session,  skip: int = 0, limit: int = 10):
    return db.query(models.Contribuitons).offset(skip).limit(limit).all()

def delete_contributions(db: Session, contribution_id: int):
    db_item = db.query(models.Contribuitons).filter(models.Contribuitons.id == contribution_id).first()
    if db_item:
        db.delete()
        db.commit()
        return {"msg": "Contribution deleted sucessfully"}
    else:
        return {"msg": "Contributions not found"}

def update_contributions(db: Session, contribution_id: int, contribution: schemas.ContriburionUpdate):
    db_item = db.query(models.Contribuitons).filter(models.Contribuitons.id == contribution_id).first()
    if db_item:
        update_data = contribution.dict(exclude_unset=True)

        for key, values in update_data.items():
            setattr(update_data, key, values)

        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return {"msg": "Contribution not found"}