from fastapi import APIRouter, HTTPException, status, Query
from fastapi import Depends
from bson import ObjectId
from typing import List, Optional
from app.schemas.campaña import CampañaCreate, CampañaOut
from app.models.campaña import Campaña
from app.db.mongo import db
from app.services import service_asignacion

from fastapi import APIRouter, Query
from app.services.campaña_service import (
    obtener_geolocalizacion_data,
    obtener_mapa_interactivo,
    obtener_alertas_de_campaña
)

router = APIRouter(prefix="/campañas", tags=["Campañas"])


# POST /campañas → Crear una nueva campaña
@router.post("/", response_model=CampañaOut)
def crear_campaña(data: CampañaCreate):
    campaña = Campaña(**data.dict())
    inserted = db["campañas"].insert_one(campaña.to_dict())
    nueva = db["campañas"].find_one({"_id": inserted.inserted_id})

    nueva["_id"] = str(nueva["_id"])
    nueva["avisador_id"] = str(nueva["avisador_id"])
    return nueva


# GET /campañas → Listar campañas con filtros básicos
@router.get("/", response_model=List[CampañaOut])
def listar_campañas(
    estado: Optional[str] = Query(None),
    buscar: Optional[str] = Query(None),
    limite: int = Query(10, gt=0)
):
    filtro = {}
    if estado:
        filtro["estado"] = estado
    if buscar:
        filtro["$or"] = [
            {"titulo": {"$regex": buscar, "$options": "i"}},
            {"marca": {"$regex": buscar, "$options": "i"}}
        ]

    campañas = db["campañas"].find(filtro).limit(limite)
    resultado = []
    for c in campañas:
        c["_id"] = str(c["_id"])
        c["avisador_id"] = str(c["avisador_id"])
        resultado.append(c)

    return resultado


# GET /campañas/{id} → Obtener campaña por ID
@router.get("/{id}", response_model=CampañaOut)
def obtener_campaña(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")

    campaña = db["campañas"].find_one({"_id": ObjectId(id)})
    if not campaña:
        raise HTTPException(status_code=404, detail="Campaña no encontrada")

    campaña["_id"] = str(campaña["_id"])
    campaña["avisador_id"] = str(campaña["avisador_id"])
    return campaña


# DELETE /campañas/{id} → Eliminar (o desactivar) campaña
@router.delete("/{id}")
def eliminar_campaña(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")

    campaña = db["campañas"].find_one({"_id": ObjectId(id)})
    if not campaña:
        raise HTTPException(status_code=404, detail="Campaña no encontrada")

    # Verifica si ya comenzó
    from datetime import datetime
    if campaña["fecha_inicio"] <= datetime.utcnow():
        raise HTTPException(status_code=403, detail="La campaña ya comenzó y no puede eliminarse")

    db["campañas"].delete_one({"_id": ObjectId(id)})

    return {"message": "Campaña eliminada correctamente"}

from fastapi import APIRouter, Query
from app.services.campaña_service import (
    obtener_geolocalizacion_data,
    obtener_mapa_interactivo,
    obtener_alertas_de_campaña
)
@router.post("/campañas/simular")
def simular_campaña(campaña: dict, usuarios: list):
    # Esto normalmente recibirá schemas, aquí simplificado
    resultado = service_asignacion.asignar_campaña_a_usuarios(campaña, usuarios)
    return resultado  # Esto lo consume el frontend para graficar

@router.get("/geolocalizacion")
def obtener_geolocalizacion(id_campaña: str = None, region: str = None, fecha_inicio: str = None, fecha_fin: str = None):
    return obtener_geolocalizacion_data(id_campaña, region, fecha_inicio, fecha_fin)

@router.get("/{id}/mapa-interactivo")
def mapa_interactivo(id: str, nivel_detalle: str = Query("medio", enum=["bajo", "medio", "alto"])):
    return obtener_mapa_interactivo(id, nivel_detalle)

@router.get("/{id}/alertas")
def obtener_alertas(id: str):
    return obtener_alertas_de_campaña(id)