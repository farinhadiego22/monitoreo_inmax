from pydantic import BaseModel
from typing import List

class ReportePais(BaseModel):
    pais: str
    usuarios: int

class ReporteSesion(BaseModel):
    pais: str
    sesiones: int

class ReporteDuracion(BaseModel):
    pais: str
    duracion: float  # en minutos o segundos

class ReporteAdquisicion(BaseModel):
    canal: str
    usuarios: int

class ReporteClicks(BaseModel):
    grupo: str  # Puede ser país, región, etc.
    clicks: int
