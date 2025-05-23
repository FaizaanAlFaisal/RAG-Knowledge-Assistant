from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

# user models

class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True
    is_admin: Optional[bool] = False

    class Config:
        from_attributes = True

class UserResponse(UserBase):
    id: int

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128, example="password123")

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128, example="password123")

class UserUpdate(BaseModel):
    password: Optional[str] = Field(None, min_length=8, max_length=128, example="password123")

class AdminUserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8, max_length=128, example="password123")
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None    

# token models

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

class TokenPayload(BaseModel):
    id: int 
    sub: str # user email
    exp: datetime | int # expiration time
    is_admin: bool
    is_active: bool