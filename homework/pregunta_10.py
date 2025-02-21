"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    resultado = []
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")
            letra = columnas[0]  # Columna 1
            elementos_col4 = len(columnas[3].split(","))  # Elementos en la columna 4
            elementos_col5 = len(columnas[4].split(","))  # Elementos en la columna 5
            resultado.append((letra, elementos_col4, elementos_col5))  # Agregar a la lista

    return resultado


# Ejecutar la función y mostrar el resultado
print(pregunta_10())
