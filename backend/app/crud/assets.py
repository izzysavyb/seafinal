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
        db: Session
):
    
    return db.query(Asset).all()

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
        asset: Asset
):
    
    try:
        logger.info(
        f"Deleting asset: {asset.id}"
        )
        db.delete(asset)
        db.commit()
        logger.info(
        f"Asset deleted successfully: {asset.id}"
        )
    
    except Exception as e:
        logger.error(
        f"Asset deletion failed: {e}"
        )   

        db.rollback()
        raise