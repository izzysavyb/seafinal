from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.deps import get_current_user
from app.crud.user import delete_user, get_all_users, get_user_by_id, update_user
from app.schemas.user import UserUpdate




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