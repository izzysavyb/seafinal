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

def update_user(db, user_id, user_data):
    user = db.execute(
        select(User).where(User.id == user_id)
    ).scalar_one_or_none()

    if not user:
        return None

    if user_data.username:
        user.username = user_data.username

    if user_data.email:
        user.email = user_data.email

    if user_data.password:
        user.password = hash_password(
            user_data.password
        )

    if user_data.role:
        user.role = user_data.role

    db.commit()
    db.refresh(user)

    return user
def delete_user(
    db: Session,
    user: User
):
    
    db.delete(user)
    db.commit()


def get_all_users(db):
    statement = select(User)

    return db.execute(
        statement).scalars().all()

def get_user_by_id(db, user_id):
    return db.execute(
        select(User).where(
            User.id == user_id
        )
    ).scalar_one_or_none()