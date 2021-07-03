from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

# hash user password
def hash_password(password):
    return pwd_cxt.hash(password)

# verify user password
def verify(hashed_password, plain_password):
    return pwd_cxt.verify(plain_password, hashed_password)
