from sqlalchemy import Column, Integer, String, Date, DateTime
from ..database import Base

# sqlalchemy model which represents the model in mysql
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), unique=True)
    dob = Column(Date)
    addresses = Column(String)
    password = Column(String(128))
    createdAt = Column(DateTime)
