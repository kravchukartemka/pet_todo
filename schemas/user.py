from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UserCreate(BaseModel):
    username: str = Field(
        min_length=1,
        max_length=50,
        description="User title"
    )

    email: EmailStr = Field(
        min_length=1,
        max_length=255,
        description="User Email"
    )

    password: str = Field(
        min_length=8,
        max_length=255,
        description="User password"
    )


class UserUpdate(BaseModel):
    user_name: str = Field(
        default=None,
        min_length=1,
        max_length=50,
        description="User title"
    )

    email: EmailStr = Field(
        min_length=1,
        default=None,
        max_length=255,
        description="User Email"
    )

    password: str = Field(
        default=None,
        min_length=8,
        max_length=255,
        description="User password"
    )


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )

