"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    asociaciones = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            valor = int(columns[1])  # Segunda columna
            letra = columns[0]  # Primera columna
            if valor not in asociaciones:
                asociaciones[valor] = set()  # Usamos un conjunto para evitar repeticiones
            asociaciones[valor].add(letra)  # Agregamos la letra
    resultado = sorted((valor, sorted(list(letras))) for valor, letras in asociaciones.items())
    return resultado


# Ejecutar la función y mostrar el resultado
print(pregunta_08())
