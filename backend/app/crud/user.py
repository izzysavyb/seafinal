from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database.models import User
from app.core.security import hash_password
from app.core.logger import logger

def get_user_by_username(
        database: Session,
        username: str
):
    return (
        database.query(User)
        .filter(User.username == username)
        .first()
    )

def get_user_by_email(
        database: Session,
        email: str
):
    return (
        database.query(User)
        .filter(User.email == email)
        .first()
    )

def create_user(
        
        database: Session,
        username: str,
        email: str,
        password: str,
        role: str = "user"
): 
    try:
        user = User(
            username = username,
            email=email,
            hashed_password=hash_password(password),
            role=role
        )
        logger.info(
            f"Creating user: {username}"
        )
        database.add(user)
        database.commit()
        database.refresh(user)
        logger.info(
            f"User created successfully: {user.id}"
        )

        return user
    except Exception as e:

        logger.error(
            f"Failed to create user: {e}"
        )
        database.rollback()

        raise HTTPException(
            status_code=500,
            detail="Failed to create user"
            
        )

def update_user(
        database: Session,
        user: User,
        update_data: dict
):
    
    for key, value in update_data.items():
        setattr(user, key, value)

    database.commit()
    database.refresh(user)

def delete_user(
    database: Session,
    user: User
):
    
    database.delete(user)
    database.commit()