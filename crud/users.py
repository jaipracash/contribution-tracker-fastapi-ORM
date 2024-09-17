from sqlalchemy.orm import Session
import schemas
import models

def create_user(db: Session, user: schemas.UserCreate):
    db_item = models.Users(name = user.name, dob = user.dob, email= user.email, address= user.address, mobile_number= user.mobile_number)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_user(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Users).offset(skip).limit(limit).all()

def delete_item(db: Session, user_id: int):
    db_item = db.query(models.Users).filter(models.Users.id == user_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return {"msg": "User deleted Sucessfully"}
    else:
        return {"msg": "User not found"}

def update_user(db: Session, user_id = int, user = schemas.UserUpdate):
    db_item = db.query(models.Users).filter(models.Users.id == user_id).first()
    if db_item:
        update_data = user.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_item, key, value)

        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return {"error": "User not found."}






