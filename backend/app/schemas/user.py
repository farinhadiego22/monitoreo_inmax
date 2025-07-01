from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Esquema para recibir login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Esquema para crear usuario (POST /users o insert manual)
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str] = None
    country: Optional[str] = None
    profile_description: Optional[str] = None
    profile_picture_url: Optional[str] = None
    birthdate: Optional[str] = None
    bank_account: Optional[str] = None
    role: str = "user"

# Esquema de respuesta segura (sin password)
class UserResponse(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    role: str

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6)
