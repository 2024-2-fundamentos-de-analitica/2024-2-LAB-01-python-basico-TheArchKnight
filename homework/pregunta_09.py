"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    conteo_claves = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")
            pares = columnas[4].split(",")  # Columna 5 (diccionario codificado)
            for par in pares:
                clave, _ = par.split(":")  # Extraemos la clave
                conteo_claves[clave] = conteo_claves.get(clave, 0) + 1  # Contamos ocurrencias

    # Retornar el diccionario ordenado por clave
    return dict(sorted(conteo_claves.items()))


# Ejecutar la función y mostrar el resultado
print(pregunta_09())
