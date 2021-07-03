from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from user_app import database, models, token
from user_app.hash import verify
from sqlalchemy.orm import Session


router = APIRouter(
    tags=['Authentication']
)

# check the existence of a user in db by checking his username and password and if the user exists,
# then the access token is being created.
@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.user.User).filter(models.user.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid Credentials")
    if not verify(user.password, request.password) and user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect password")

    access_token = token.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
