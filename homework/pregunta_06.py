"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    valores_diccionario = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")
            pares = columnas[4].split(",")  # Columna 5
            for par in pares:
                clave, valor = par.split(":")
                valor = int(valor)
                if clave in valores_diccionario:
                    valores_diccionario[clave].append(valor)
                else:
                    valores_diccionario[clave] = [valor]
    resultado = sorted((clave, min(valores_diccionario[clave]),
                        max(valores_diccionario[clave]))
                       for clave in valores_diccionario)
    return resultado


# Ejecutar la función y mostrar el resultado
print(pregunta_06())
