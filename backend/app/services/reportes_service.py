from datetime import date
from typing import List

# Datos mockeados de prueba
def obtener_top_usuarios_por_pais(top_n: int, fecha_inicio: date, fecha_fin: date):
    return [
        {"pais": "Chile", "usuarios": 1200},
        {"pais": "Argentina", "usuarios": 950},
        {"pais": "México", "usuarios": 800}
    ][:top_n]

def obtener_top_sesiones_por_pais(top_n: int, fecha_inicio: date, fecha_fin: date):
    return [
        {"pais": "Chile", "sesiones": 3000},
        {"pais": "Colombia", "sesiones": 2800},
        {"pais": "México", "sesiones": 2500}
    ][:top_n]

def obtener_duracion_promedio(fecha_inicio: date, fecha_fin: date):
    return [
        {"pais": "Chile", "duracion": 4.2},
        {"pais": "Argentina", "duracion": 3.7},
        {"pais": "Perú", "duracion": 3.1}
    ]

def obtener_adquisicion_usuarios(fecha_inicio: date, fecha_fin: date):
    return [
        {"canal": "social", "usuarios": 1500},
        {"canal": "direct", "usuarios": 1100},
        {"canal": "orgánico", "usuarios": 950}
    ]

def obtener_clicks_por_pais(fecha_inicio: date, fecha_fin: date):
    return [
        {"grupo": "Chile", "clicks": 3200},
        {"grupo": "México", "clicks": 2400},
        {"grupo": "Argentina", "clicks": 1800}
    ]
