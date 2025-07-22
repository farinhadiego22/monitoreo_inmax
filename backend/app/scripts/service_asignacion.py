# services/service_asignacion.py

import random

def asignar_campaña_a_usuarios(campaña, usuarios, monto_por_interaccion=1):
    """Asigna campaña a usuarios elegidos, simula interacciones y calcula bono/presupuesto."""

    resultados = []
    presupuesto_restante = campaña["presupuesto"]

    for usuario in usuarios:
        # Ejemplo: Probabilidad de ser seleccionado crece con amigos (puedes hacerla más avanzada)
        probabilidad = min(usuario["amigos"] / 500, 1.0)
        if random.random() < probabilidad:
            # Número de interacciones simuladas usando ipp histórico y algo de aleatoriedad
            interacciones = int(random.gauss(usuario["ipp"], usuario["ipp"] * 0.15))
            interacciones = max(0, interacciones)  # Evita negativos

            bono = interacciones * monto_por_interaccion

            if presupuesto_restante >= bono:
                presupuesto_restante -= bono
                resultados.append({
                    "username": usuario["username"],
                    "interacciones": interacciones,
                    "bono": bono,
                    "amigos": usuario["amigos"],
                    "edad": usuario["edad"],
                    "pais": usuario["pais"],
                })
            else:
                # Si no alcanza presupuesto, asigna lo que quede
                if presupuesto_restante > 0:
                    interacciones_posibles = presupuesto_restante // monto_por_interaccion
                    bono = interacciones_posibles * monto_por_interaccion
                    resultados.append({
                        "username": usuario["username"],
                        "interacciones": int(interacciones_posibles),
                        "bono": bono,
                        "amigos": usuario["amigos"],
                        "edad": usuario["edad"],
                        "pais": usuario["pais"],
                    })
                    presupuesto_restante = 0
                break

    # KPIs globales para gráficos
    kpis = {
        "campaña": campaña["nombre"],
        "usuarios_seleccionados": len(resultados),
        "total_interacciones": sum(r["interacciones"] for r in resultados),
        "total_bonos": sum(r["bono"] for r in resultados),
        "presupuesto_restante": presupuesto_restante,
        # Para gráficos por segmento
        "interacciones_por_edad": agrupar_por(resultados, "edad"),
        "interacciones_por_pais": agrupar_por(resultados, "pais"),
        "interacciones_por_usuario": {r["username"]: r["interacciones"] for r in resultados},
    }

    return {"detalle": resultados, "kpis": kpis}


def agrupar_por(lista, campo):
    """Devuelve un diccionario con sumatoria de interacciones por campo."""
    resultado = {}
    for item in lista:
        key = item[campo]
        resultado[key] = resultado.get(key, 0) + item["interacciones"]
    return resultado
