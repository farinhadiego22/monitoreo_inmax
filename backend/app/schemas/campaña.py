from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from datetime import datetime

class CampañaCreate(BaseModel):
    avisador_id: str = Field(..., description="ID del avisador que crea la campaña")
    costo: float = Field(..., gt=0, description="Costo total de la campaña")
    marca: str
    titulo: str
    descripcion_producto: str
    link_producto: HttpUrl
    fecha_inicio: datetime
    fecha_fin: datetime
    imagenes: Optional[List[HttpUrl]] = []
    videos: Optional[List[HttpUrl]] = []

class CampañaOut(BaseModel):
    id: str = Field(..., alias="_id")
    avisador_id: str
    costo: float
    marca: str
    titulo: str
    descripcion_producto: str
    link_producto: HttpUrl
    fecha_inicio: datetime
    fecha_fin: datetime
    imagenes: List[HttpUrl]
    videos: List[HttpUrl]
    estado: str = "activa"
