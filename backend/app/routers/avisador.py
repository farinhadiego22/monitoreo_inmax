from fastapi import APIRouter, HTTPException, status
from app.schemas.avisador import AvisadorCreate, AvisadorOut
from app.models.avisador import Avisador
from app.db.mongo import db
from bson import ObjectId

router = APIRouter(prefix="/avisadores", tags=["Avisadores"])

# POST /avisadores
@router.post("/", response_model=AvisadorOut)
def crear_avisador(data: AvisadorCreate):
    nuevo_avisador = Avisador(**data.dict())
    result = db["avisadores"].insert_one(nuevo_avisador.to_dict())

    avisador = db["avisadores"].find_one({"_id": result.inserted_id})
    avisador["_id"] = str(avisador["_id"])
    avisador["usuario_id"] = str(avisador["usuario_id"])
    return avisador


# GET /avisadores
@router.get("/", response_model=list[AvisadorOut])
def listar_avisadores():
    avisadores = db["avisadores"].find()
    resultado = []
    for a in avisadores:
        a["_id"] = str(a["_id"])
        a["usuario_id"] = str(a["usuario_id"])
        resultado.append(a)
    return resultado
