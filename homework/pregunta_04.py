"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    conteo_meses = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            fecha = line.strip().split("\t")[2]  # Tercera columna
            mes = fecha.split("-")[1]  # Extraer el mes
            conteo_meses[mes] = conteo_meses.get(mes, 0) + 1
    resultado = sorted(conteo_meses.items())  # Ordenar por mes
    return resultado


# Ejecutar la función y mostrar el resultado
print(pregunta_04())
