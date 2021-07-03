from datetime import datetime, timedelta
from jose import JWTError, jwt
from . import schemas
from .constants import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception

        schemas.authentication.TokenData(username=username)

    except JWTError:
        raise credentials_exception
