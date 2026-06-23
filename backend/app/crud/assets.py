from fastapi import HTTPException
from sqlalchemy import select

from app.core.logger import logger
from sqlalchemy.orm import Session
from app.database.models import Asset
from app.schemas.asset import AssetCreate

def create_asset(
        db: Session,
        asset_data: AssetCreate,
        owner_id: int
):
    try:  
        asset = Asset(
            name=asset_data.name,
            category=asset_data.category,
            serial_number=asset_data.serial_number,
            status=asset_data.status,
            owner_id=owner_id 
        )
        logger.info(
            f"Creating asset: {asset_data.serial_number}"
        )
        db.add(asset)
        db.commit()
        db.refresh(asset)
        logger.info(
            f"Asset created successfully: {asset.id}"
        )
        return asset
    except Exception as e:
        logger.error(
        f"Asset creation failed: {e}"
    )
        db.rollback()
        raise
def get_assets(
        db: Session,
        current_user: dict
):
    
    if current_user["role"] == "admin":
        statement = select(Asset)
        
    else: 
        statement = (
            select(Asset).where(Asset.owner_id == current_user["id"])
        )
    result = db.execute(statement)
    return result.scalars().all()

def get_asset(
        db: Session,
        asset_id: int
):
    
    return(
        db.query(Asset)
        .filter(Asset.id == asset_id)
        .first()
    )

def update_asset(
        db: Session,
        asset: Asset,
        update_data: dict
):
    try:
        logger.info(
        f"Updating asset: {asset.id}"
        )
        for key, value in update_data.items():
            setattr(asset, key, value)

            db.commit()
            db.refresh(asset)
            logger.info(
            f"Asset updated successfully: {asset.id}"
                )

            return asset
    except Exception as e:
        logger.error(
        f"Asset update failed: {e}"
        )

        db.rollback()
        raise


def delete_asset(
    db: Session,
    asset_id: int,
    current_user: dict
):
    statement = (
        select(Asset)
        .where(Asset.id == asset_id)
    )

    result = db.execute(statement)

    asset = result.scalar_one_or_none()

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found"
        )

    if (
        current_user["role"] != "admin"
        and asset.owner_id != current_user["id"]
    ):
        raise HTTPException(
            status_code=403,
            detail="Not authorised"
        )

    db.delete(asset)
    db.commit()

    return {
        "message":
        "Asset deleted"
    }