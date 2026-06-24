from fastapi import ( APIRouter, Depends, HTTPException)
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.asset import AssetCreate, AssetUpdate
from app.crud.assets import (create_asset, get_assets, get_asset, update_asset, delete_asset)
from app.core.deps import ( get_current_user, require_role)
from app.database.models import Asset

router = APIRouter()

@router.get("/")
def list_assets(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_assets(db, current_user)

@router.get("/{asset_id}")
def get_asset_by_id(
    asset_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    
    asset = get_asset(
        db,
        asset_id
    )

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found"
        )
    return asset

@router.post("/")
def create_asset_route(
    asset_data: AssetCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_asset(
        db,
        asset_data,
        current_user["id"]
    )

@router.put("/{asset_id}")
def update_asset_route(
    asset_id: int,
    asset_data: AssetUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    asset = db.get(
        Asset,
        asset_id
    )

 

    if asset_data.name is not None:
        asset.name = asset_data.name

    if asset_data.category is not None:
        asset.category = asset_data.category

    if asset_data.status is not None:
        asset.status = asset_data.status

    if asset_data.owner_id is not None:
        asset.owner_id = asset_data.owner_id

    db.commit()
    db.refresh(asset)

    return asset

@router.delete("/{asset_id}")
def delete_asset_route(
    asset_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_role("admin")
    )
):

    asset = get_asset(
        db,
        asset_id
    )

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found"
        )

    return delete_asset(
        db,
        asset_id,
        current_user
    )


 