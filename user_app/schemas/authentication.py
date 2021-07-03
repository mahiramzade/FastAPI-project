from typing import Optional
from pydantic import BaseModel

# pydantic Login model
class Login(BaseModel):
    username: str
    password: str

# pydantic Token model
class Token(BaseModel):
    access_token: str
    token_type: str

# pydantic TokenData model
class TokenData(BaseModel):
    username: Optional[str] = None
