from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_password(password):
    return pwd_cxt.hash(password)
