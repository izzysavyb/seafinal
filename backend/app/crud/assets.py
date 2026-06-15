from app.core.logger import logger
from sqlalchemy.orm import Session
from app.database.models import Asset

def create_asset(
        database: Session,
        asset_data
):
    try:  
        asset = Asset(
            **asset_data.model_dump()
        )
        logger.info(
            f"Creating asset: {asset_data.serial_number}"
        )
        database.add(asset)
        database.commit()
        database.refresh(asset)
        logger.info(
            f"Asset created successfully: {asset.id}"
        )
        return asset
    except Exception as e:
        logger.error(
        f"Asset creation failed: {e}"
    )
        database.rollback

def get_assets(
        database: Session
):
    
    return database.query(Asset).all()

def get_asset(
        database: Session,
        asset_id: int
):
    
    return(
        database.query(Asset)
        .filter(Asset.id == asset_id)
        .first()
    )

def update_asset(
        database: Session,
        asset: Asset,
        update_data: dict
):
    try:
        logger.info(
        f"Updating asset: {asset.id}"
        )
        for key, value in update_data.items():
            setattr(asset, key, value)

            database.commit()
            database.refresh(asset)
            logger.info(
            f"Asset updated successfully: {asset.id}"
                )

            return asset
    except Exception as e:
        logger.error(
        f"Asset update failed: {e}"
        )

        database.rollback


def delete_asset(
        database: Session,
        asset: Asset
):
    
    try:
        logger.info(
        f"Deleting asset: {asset.id}"
        )
        database.delete(asset)
        database.commit()
        logger.info(
        f"Asset deleted successfully: {asset.id}"
        )
    
    except Exception as e:
        logger.error(
        f"Asset deletion failed: {e}"
        )   

        database.rollback