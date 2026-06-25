from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database.models import Asset, User
from app.core.security import hash_password
from app.core.logger import logger
from app.schemas.user import UserUpdate

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

def update_user(db: Session, user_id: int, user_data: UserUpdate):
    user = db.execute(
        select(User).where(User.id == user_id)
    ).scalar_one_or_none()

    if not user:
        return None

    update_data = user_data.model_dump(exclude_unset=True)

    if "username" in update_data:
        user.username = update_data["username"]

    if "email" in update_data:
        user.email = update_data["email"]

    if "password" in update_data:
        user.hashed_password = hash_password(update_data["password"])

    if "role" in update_data:
        user.role = update_data["role"]

    db.commit()
    db.refresh(user)

    return user

def delete_user(db: Session, user_id: int, current_user: dict):
    

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
  

    owned_assets = db.query(Asset).filter(Asset.owner_id == user.id).first()

    if owned_assets:
        raise HTTPException(
            status_code=400,
            detail="Cannot delete user while they still own assets -  please transfer or delete these assets"
        )


    db.delete(user)
    db.commit()

    return {
        "message": "User deleted and assets transferred"
    }

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