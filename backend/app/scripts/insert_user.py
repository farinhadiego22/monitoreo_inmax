import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.mongo import db
from utils.security import hash_password

# Datos del nuevo usuario
usuario = {
    "email": "admin@inmax.com",
    "hashed_password": hash_password("admin123"),
    "role": "admin",
    "name": "Administrador Inmax",
    "country": "Chile",
    "profile_description": "Usuario de prueba",
    "profile_picture_url": None,
    "birthdate": "1990-01-01",
    "bank_account": "123456789"
}

# Insertar en la colección "users"
result = db["users"].insert_one(usuario)
print(f"✅ Usuario insertado con ID: {result.inserted_id}")
