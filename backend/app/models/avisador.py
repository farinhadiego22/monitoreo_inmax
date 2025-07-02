from typing import Optional
from datetime import datetime
from bson import ObjectId

class Avisador:
    def __init__(
        self,
        usuario_id: str,
        id_empresa: str,
        categoria_comercial: str,
        metodo_pago: str,
        link_producto: Optional[str] = None,
        fecha: Optional[datetime] = None
    ):
        self.usuario_id = ObjectId(usuario_id)
        self.id_empresa = id_empresa
        self.categoria_comercial = categoria_comercial
        self.metodo_pago = metodo_pago
        self.link_producto = link_producto
        self.fecha = fecha or datetime.utcnow()

    def to_dict(self):
        return {
            "usuario_id": self.usuario_id,
            "id_empresa": self.id_empresa,
            "categoria_comercial": self.categoria_comercial,
            "metodo_pago": self.metodo_pago,
            "link_producto": self.link_producto,
            "fecha": self.fecha
        }
