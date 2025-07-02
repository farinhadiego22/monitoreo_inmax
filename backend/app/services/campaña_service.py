def obtener_geolocalizacion_data(id_campaña, region, fecha_inicio, fecha_fin):
    # Acá puede ir lógica real con Mongo si luego se requiere
    return [
        {"lat": -33.4489, "lon": -70.6693, "ciudad": "Santiago", "impresiones": 1035},
        {"lat": -36.8201, "lon": -73.0444, "ciudad": "Concepción", "impresiones": 432}
    ]

def obtener_mapa_interactivo(id, nivel_detalle):
    zonas = {
        "bajo": [{"zona": "Chile Central", "usuarios": 1200}],
        "medio": [{"zona": "RM", "usuarios": 750}],
        "alto": [{"zona": "Santiago Centro", "usuarios": 400}]
    }
    return {
        "nivel": nivel_detalle,
        "zonas": zonas.get(nivel_detalle, [])
    }

def obtener_alertas_de_campaña(id):
    return {
        "alertas": [
            {"tipo": "presupuesto", "umbral": 1000, "uso_actual": 850, "activo": True}
        ]
    }
