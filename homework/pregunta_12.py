"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    suma_col5 = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")
            letra = columnas[0]  # Columna 1
            valores_col5 = columnas[4].split(",")  # Columna 5 (diccionarios clave:valor)
            suma = sum(int(par.split(":")[1]) for par in valores_col5)  # Sumar valores de la columna 5
            suma_col5[letra] = suma_col5.get(letra, 0) + suma  # Acumular la suma

    resultado = dict(sorted(suma_col5.items()))  # Ordenar alfabéticamente
    return resultado


# Ejecutar la función y mostrar el resultado
print(pregunta_12())
