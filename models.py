from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db import Base
from datetime import date

class Users(Base):
    _tablename_ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable = False, index=True)
    dob = Column(date)
    email = Column(String(250), nullable=False, unique=True)
    address = Column(String(250))
    mobile_number = Column(String(10), unique=True)

    def __repr__(self):
        return f"<Users(id = {self.id}, name = {self.name}, email = {self.email}, mobile_number = {self.mobile_number}"

class Events(Base):
    _tablename_ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(users.id), nullable=False)
    name = Column(String(300), nullable=False)
    date = Column(Date)
    location = Column(String(300), nullable=False)

    def __repr__(self):
        return f"<Events(id = {self.id}, user_id = {self.user_id}, name = {self.name}, date = {self.date}, location = {self.location}"

class Contribuitons(Base):
    _tablename_ = 'contributions'

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey(events.id), nullable=False)
    name = Column(String(100))
    address = Column(String(300))
    amount = Column(String(10), nullable=False)
    mobile_number = Column(String(10))

    def __repr__(self):
        return f"<Contributions(id = {self.id}, event_id = {self.event_id}, name = {self.name}, amount ={self.amount}"

























