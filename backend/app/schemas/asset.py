from pydantic import BaseModel, ConfigDict, Field

class AssetCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100
    )
    category: str = Field(
        min_length=2,
        max_length=50
    )
    serial_number: str
    status: str
    
    


class AssetUpdate(BaseModel):
    name: str | None = None
    cateory: str | None = None
    


class AssetOut(BaseModel):
    id: int
    name: str
    category: str
    serial_number: str
    status: str
    owner_id: int

    model_config = ConfigDict(from_attributes = True)