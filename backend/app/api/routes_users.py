from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.deps import get_current_user
from app.crud.user import delete_user, get_all_users, get_user_by_id, update_user
from app.schemas.user import UserUpdate
from app.database.models import User
from app.core.security import hash_password




router = APIRouter()

@router.get("/")
def get_users_route(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Not Authorised"
        )
    return get_all_users(db)

@router.get("/me")
def get_my_account(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    user = get_user_by_id(db, current_user["id"])

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

@router.put("/me")
def update_my_account(
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    user = db.query(User).filter(
        User.id == current_user["id"]
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.username = user_data.username
    user.email = user_data.email

    if user_data.password:
        user.password = hash_password(user_data.password)

    db.commit()
    db.refresh(user)

    return user

@router.put("/{user_id}")
def update_user_route(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if (
        current_user["id"] != user_id
        and current_user["role"] != "admin"
    ):
        raise HTTPException(
            status_code=403,
            detail="Not authorised"
        )

    return update_user(
        db,
        user_id,
        user_data)

@router.get("/{user_id}")
def get_user_route(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_user_by_id(
        db,
        user_id
    )

@router.delete("/{user_id}")
def delete_user_route(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admins only"
        )

    return delete_user(db, user_id, current_user)