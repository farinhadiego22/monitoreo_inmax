from fastapi import APIRouter, Query, HTTPException
from datetime import date
from typing import Optional, List

from app.schemas.reportes import (
    ReportePais,
    ReporteSesion,
    ReporteDuracion,
    ReporteAdquisicion,
    ReporteClicks
)

import app.services.reportes_service as reportes_service


router = APIRouter(prefix="/reportes", tags=["Reportes"])

@router.get("/usuarios-top-paises", response_model=List[ReportePais])
def usuarios_top_paises(
    top_n: int = Query(..., gt=0),
    fecha_inicio: Optional[date] = None,
    fecha_fin: Optional[date] = None
):
    return reportes_service.obtener_top_usuarios_por_pais(top_n, fecha_inicio, fecha_fin)


@router.get("/sesiones-top-paises", response_model=List[ReporteSesion])
def sesiones_top_paises(
    top_n: int = Query(..., gt=0),
    fecha_inicio: Optional[date] = None,
    fecha_fin: Optional[date] = None
):
    return reportes_service.obtener_top_sesiones_por_pais(top_n, fecha_inicio, fecha_fin)


@router.get("/duracion-promedio-pais", response_model=List[ReporteDuracion])
def duracion_promedio_pais(
    fecha_inicio: date,
    fecha_fin: date
):
    return reportes_service.obtener_duracion_promedio(fecha_inicio, fecha_fin)


@router.get("/adquisicion-usuarios", response_model=List[ReporteAdquisicion])
def adquisicion_usuarios(
    fecha_inicio: date,
    fecha_fin: date
):
    return reportes_service.obtener_adquisicion_usuarios(fecha_inicio, fecha_fin)


@router.get("/clicks-pais", response_model=List[ReporteClicks])
def clicks_por_pais(
    fecha_inicio: date,
    fecha_fin: date
):
    return reportes_service.obtener_clicks_por_pais(fecha_inicio, fecha_fin)
