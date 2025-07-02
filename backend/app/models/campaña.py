from typing import Optional, List
from datetime import datetime
from bson import ObjectId

class Campaña:
    def __init__(
        self,
        avisador_id: str,
        costo: float,
        marca: str,
        titulo: str,
        descripcion_producto: str,
        link_producto: str,
        fecha_inicio: datetime,
        fecha_fin: datetime,
        imagenes: Optional[List[str]] = None,
        videos: Optional[List[str]] = None,
        estado: str = "activa"
    ):
        self.avisador_id = ObjectId(avisador_id)
        self.costo = costo
        self.marca = marca
        self.titulo = titulo
        self.descripcion_producto = descripcion_producto
        self.link_producto = link_producto
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.imagenes = imagenes or []
        self.videos = videos or []
        self.estado = estado

    def to_dict(self):
        return {
            "avisador_id": self.avisador_id,
            "costo": self.costo,
            "marca": self.marca,
            "titulo": self.titulo,
            "descripcion_producto": self.descripcion_producto,
            "link_producto": self.link_producto,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin,
            "imagenes": self.imagenes,
            "videos": self.videos,
            "estado": self.estado
        }
