from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from datetime import datetime

class AvisadorCreate(BaseModel):
    usuario_id: str = Field(..., description="ID del usuario que actúa como avisador")
    id_empresa: str = Field(..., description="Identificador único de la empresa")
    categoria_comercial: str
    metodo_pago: str
    link_producto: Optional[HttpUrl] = None
    fecha: Optional[datetime] = None

class AvisadorOut(BaseModel):
    id: str = Field(..., alias="_id")
    usuario_id: str
    id_empresa: str
    categoria_comercial: str
    metodo_pago: str
    link_producto: Optional[HttpUrl] = None
    fecha: Optional[datetime] = None
