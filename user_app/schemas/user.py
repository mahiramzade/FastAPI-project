import datetime

from pydantic import BaseModel

from typing import Optional, List

# pydantic User model
class User(BaseModel):
    username: str
    dob: datetime.date
    addresses: Optional[List[str]] = None
    password: str
    createdAt: datetime.datetime

# pydantic ShowUser model (to show only necessary fields)
class ShowUser(BaseModel):
    id: int
    username: str
    dob: datetime.date
    addresses: Optional[str] = None
    createdAt: datetime.datetime

    class Config:
        orm_mode = True
