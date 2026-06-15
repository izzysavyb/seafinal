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
    owner_id: int
    


class AssetUpdate(BaseModel):
    name: str | None = None
    cateory: str | None = None
    is_active: bool | None =  None


class AssetOut(BaseModel):
    id: int
    name: str
    category: str
    serial_number: str
    is_active: bool
    owner_id: int

    model_config = ConfigDict(from_attributes = True)