"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    suma_letras = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")
            valor = int(columnas[1])  # Columna 2 (valor numérico)
            letras_col4 = columnas[3].split(",")  # Letras de la columna 4

            for letra in letras_col4:
                suma_letras[letra] = suma_letras.get(letra, 0) + valor  # Sumar valores
    resultado = dict(sorted(suma_letras.items()))  # Ordenar alfabéticamente
    return resultado


# Ejecutar la función y mostrar el resultado
print(pregunta_11())
