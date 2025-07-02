from app.db.mongo import db
from datetime import datetime, timedelta
from bson import ObjectId

print("Insertando campañas de prueba...")

avisador_id = ObjectId()  # Si tienes uno real, reemplázalo aquí

campañas = [
    {
        "avisador_id": avisador_id,
        "costo": 1500,
        "marca": "Nike",
        "titulo": "Lanzamiento Verano",
        "descripcion_producto": "Zapatillas edición verano",
        "link_producto": "https://nike.cl/zapa123",
        "fecha_inicio": datetime.utcnow() + timedelta(days=1),
        "fecha_fin": datetime.utcnow() + timedelta(days=30),
        "imagenes": ["https://cdn.inmax.cl/banner1.jpg"],
        "videos": ["https://cdn.inmax.cl/spot1.mp4"],
        "estado": "activa"
    },
    {
        "avisador_id": avisador_id,
        "costo": 950,
        "marca": "Samsung",
        "titulo": "Promo Galaxy",
        "descripcion_producto": "Galaxy S30 Ultra con descuento",
        "link_producto": "https://samsung.com/galaxyS30",
        "fecha_inicio": datetime.utcnow() + timedelta(days=3),
        "fecha_fin": datetime.utcnow() + timedelta(days=20),
        "imagenes": ["https://cdn.inmax.cl/banner2.jpg"],
        "videos": [],
        "estado": "activa"
    },
    {
        "avisador_id": avisador_id,
        "costo": 300,
        "marca": "Falabella",
        "titulo": "Cyberday Moda",
        "descripcion_producto": "Ofertas en ropa",
        "link_producto": "https://falabella.cl/cybermoda",
        "fecha_inicio": datetime.utcnow() + timedelta(days=5),
        "fecha_fin": datetime.utcnow() + timedelta(days=10),
        "imagenes": [],
        "videos": [],
        "estado": "activa"
    }
]

resultado = db["campañas"].insert_many(campañas)
print(f"Se insertaron {len(resultado.inserted_ids)} campañas.")
