from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.database.database import get_db
from app.schemas.user import (
    UserCreate,
    UserLogin
)
from app.crud.user import ( 
    create_user,
    get_user_by_email,
    get_user_by_username
    )
from app.core.security import (
    verify_password,
    create_access_token
)

router = APIRouter()

@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    exisiting_user = get_user_by_username(
        db,
        user.username
    )

    if exisiting_user:
        raise HTTPException(
            status_code=409,
            detail="Username already exists"
        )
    
    exisiting_email = get_user_by_email(
        db,
        user.email
    )

    if exisiting_email:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )
    
    new_user = create_user(
        db=db,
        username=user.username,
        email=user.email,
        password=user.password
    )

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = get_user_by_username(
        db,
        form_data.username
    )
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    
    if not verify_password(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
    
    token = create_access_token(
        {
            "sub": user.username,
            "role": user.role,
            "id": user.id
        }
    )
    

    return {
        "access_token": token,
        "token_type": "bearer"
        
    }