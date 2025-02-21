"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    suma = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            letra = columns[0]  # Primera columna
            valor = int(columns[1])  # Segunda columna
            suma[letra] = suma.get(letra, 0) + valor
    resultado = sorted(suma.items())  # Ordenar alfabéticamente
    return resultado


# Ejecutar la función y mostrar el resultado
print(pregunta_03())
