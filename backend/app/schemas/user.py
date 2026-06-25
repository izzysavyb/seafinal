from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel): 
    username: str = Field(
        min_length=3,
        max_length=50
    )
    email: EmailStr 
    password: str = Field(
        min_length=8,
        max_length=128
    )


class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    model_config =  ConfigDict (from_attributes = True)

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3)
    email: Optional[EmailStr] = None
    password: Optional[str] | None = None
    role: Literal["admin", "user"] | None = None