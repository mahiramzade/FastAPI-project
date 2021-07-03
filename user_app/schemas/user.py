import datetime

from pydantic import BaseModel

from typing import Optional, List


class User(BaseModel):
    username: str
    dob: datetime.date
    addresses: Optional[List[str]] = None
    password: str
    createdAt: datetime.datetime


class ShowUser(BaseModel):
    id: int
    username: str
    dob: datetime.date
    addresses: Optional[List[str]] = None
    createdAt: datetime.datetime

    class Config:
        orm_mode = True
