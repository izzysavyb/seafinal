from typing import Literal

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
    username: str | None = None
    email: EmailStr | None = None
    role: Literal["admin", "user"] | None = None