from fastapi import status, Depends, APIRouter
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from typing import List
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
from .. import auth_check

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login", response_model=schemas.Token)
def login_user(userCred: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.email == userCred.username).first()
    if user == None:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="User not found")

    if not utils.verifyPass(userCred.password, user.password):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Incorrect password")
    access_token = auth_check.create_access_token(data = {"userid": user.id});
    return {"access_token": access_token, "token_type":"bearer"}

    