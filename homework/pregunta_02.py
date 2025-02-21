"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    conteo = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            letra = line.strip().split("\t")[0]  # Primera columna
            conteo[letra] = conteo.get(letra, 0) + 1
    resultado = sorted(conteo.items())  # Ordenar alfabéticamente
    return resultado


# Ejecutar la función y mostrar el resultado
print(pregunta_02())
