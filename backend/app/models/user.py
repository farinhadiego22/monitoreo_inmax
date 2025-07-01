from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    email: EmailStr
    hashed_password: str
    role: str = "user"

    # Campos opcionales del modelo conceptual
    name: Optional[str] = None
    country: Optional[str] = None
    profile_description: Optional[str] = None
    profile_picture_url: Optional[str] = None
    birthdate: Optional[str] = None
    bank_account: Optional[str] = None
