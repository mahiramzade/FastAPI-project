import datetime
from typing import List

from fastapi import Depends, status, APIRouter, HTTPException
from sqlalchemy.orm import Session

from user_app import hash
from user_app.models.user import User as mUser
from user_app.schemas.user import User as sUser
from user_app.schemas.user import ShowUser
from user_app.oauth2 import get_current_user
from user_app.database import get_db

router = APIRouter(
    tags=['users'],
    prefix='/user',
)


@router.post('', status_code=status.HTTP_201_CREATED)
def create_user(request: sUser, db: Session = Depends(get_db)):
    new_user = mUser(username=request.username, dob=request.dob, password=hash.hash_password(request.password),
                     addresses=request.addresses, createdAt=datetime.datetime.now())

    if db.query(mUser).filter(mUser.username == new_user.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='The given username already exists.')

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/list', status_code=status.HTTP_200_OK, response_model=List[ShowUser])
def get_users_list(db: Session = Depends(get_db), curren_user: sUser = Depends(get_current_user)):
    return db.query(mUser).all()


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_specific_user(id, db: Session = Depends(get_db), curren_user: sUser = Depends(get_current_user)):
    user = db.query(mUser).filter(mUser.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The User with id {id} is not found')

    return user


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_user(id, db: Session = Depends(get_db), curren_user: sUser = Depends(get_current_user)):
    user = db.query(mUser).filter(mUser.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The User with the id {id} is not found')

    user.delete()
    db.commit()

    return f'The User with id {id} is deleted'


@router.patch('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(id, request: sUser, db: Session = Depends(get_db), curren_user: sUser = Depends(get_current_user)):
    user = db.query(mUser).filter(mUser.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The User with the id {id} is not found')

    # user.update(request.dict())
    user.update({'username': request.username, 'dob': request.dob, 'addresses': request.addresses,
                 'password': hash.hash_password(request.password)})
    db.commit()

    return user.first()
