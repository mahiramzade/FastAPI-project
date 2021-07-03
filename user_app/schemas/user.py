import datetime

from pydantic import BaseModel

from typing import Optional


class User(BaseModel):
    username: str
    dob: datetime.date
    addresses: Optional[str] = None
    password: str
    createdAt: datetime.datetime


class ShowUser(BaseModel):
    username: str
    dob: datetime.date
    addresses: Optional[str] = None
    createdAt: datetime.datetime

    class Config:
        orm_mode = True
