from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database.models import User
from app.core.security import hash_password
from app.core.logger import logger

def get_user_by_username(
        db: Session,
        username: str
):
    return db.execute(
            select(User).where(
                User.username == username
            )
     
    ).scalar_one_or_none()

def get_user_by_email(
        db: Session,
        email: str
):
      return db.execute(
            select(User).where(
                User.email == email
            )
     
    ).scalar_one_or_none()


def create_user(
        
        db: Session,
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
        db.add(user)
        db.commit()
        db.refresh(user)
        logger.info(
            f"User created successfully: {user.id}"
        )

        return user
    except Exception as e:

        logger.error(
            f"Failed to create user: {e}"
        )
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Failed to create user"
            
        )

def update_user(
        db: Session,
        user: User,
        update_data: dict
):
    
    for key, value in update_data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

def delete_user(
    db: Session,
    user: User
):
    
    db.delete(user)
    db.commit()