"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    asociaciones = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            valor = int(columns[1])  # Segunda columna
            letra = columns[0]  # Primera columna
            if valor in asociaciones:
                asociaciones[valor].append(letra)
            else:
                asociaciones[valor] = [letra]

    resultado = sorted(asociaciones.items())
    return resultado


# Ejecutar la función y mostrar el resultado
print(pregunta_07())
