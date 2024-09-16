from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    dob: str
    email: str
    address: str
    mobile_number: str
    
class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

class UserUpdate(BaseModel):
    name: optional[str] = None
    dob: optional[str] = None
    email: optional[str] = None
    address: optional[str] = None
    mobile_number: optional[str] = None

class EventBase(BaseModel):
    user_id: int
    name: str
    date: str
    location: str

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int


class ContributionBase(BaseModel):
    event_id: int
    name: str
    address: str
    amount: str
    mobile_number: str

class ContributionCreate(ContributionBase):
    pass

class Contribution(ContributionBase):
    id: int


class Config:
    orm_mode = True