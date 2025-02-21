"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    valores = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            letra = columns[0]  # Primera columna
            valor = int(columns[1])  # Segunda columna
            if letra in valores:
                valores[letra].append(valor)
            else:
                valores[letra] = [valor]
    resultado = sorted((letra, max(valores[letra]), min(valores[letra])) for letra in valores)
    return resultado


# Ejecutar la función y mostrar el resultado
print(pregunta_05())
