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
    name: Optional[str] = None
    dob: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    mobile_number: Optional[str] = None

class EventBase(BaseModel):
    user_id: int
    name: str
    date: str
    location: str

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

class EventUpdate(BaseModel):
    user_id: Optional[str] = None
    name: Optional[str] = None
    date: Optional[str] = None
    location: Optional[str] = None


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