from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from app.utils.security import get_current_user
from app.schemas.user import UserLogin, UserCreate
from app.utils.security import verify_password, create_access_token, hash_password
from app.db.mongo import db
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])

# Login para Swagger/OpenAPI (usa form-data)
@router.post("/login")
def login_form(form_data: OAuth2PasswordRequestForm = Depends()):
    user_data = db["users"].find_one({"email": form_data.username})

    if not user_data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado")

    if not verify_password(form_data.password, user_data["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Contraseña incorrecta")

    token = create_access_token(
        data={"sub": form_data.username},
        expires_delta=timedelta(minutes=60)
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "email": user_data["email"],
        "role": user_data.get("role", "user"),
        "name": user_data.get("name")
    }

# Login para el frontend Vue (usa JSON)
@router.post("/frontend-login")
def frontend_login(user: UserLogin):
    user_data = db["users"].find_one({"email": user.email})
    
    if not user_data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado")

    if not verify_password(user.password, user_data["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Contraseña incorrecta")
    
    token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=60)
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "email": user_data["email"],
        "role": user_data.get("role", "user"),
        "name": user_data.get("name")
    }
@router.post("/register")
def register(user: UserCreate):
    existing_user = db["users"].find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuario ya registrado")

    hashed_pw = hash_password(user.password)
    new_user = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_pw,
        "role": "user",
        "name": user.username
    }

    db["users"].insert_one(new_user)
    access_token = create_access_token(data={"sub": user.email})

    return {
        "message": "Usuario registrado correctamente",
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_current_user_info(current_user: dict = Depends(get_current_user)):
    return {
        "email": current_user["email"],
        "role": current_user.get("role", "user"),
        "name": current_user.get("name")
    }

