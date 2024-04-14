import random
import pandas as pd
from pathlib import Path
import os
import numpy as np

def obtener_valor_inicial(valor_objetivo,ruta):
    valor_objetivo = float(valor_objetivo)
    df = pd.read_csv(ruta)
    df['Diferencia'] = abs(df['Medidor [W]'] - valor_objetivo)
    valor_cercano = df.loc[df['Diferencia'].idxmin()]
    
    fila_correspondiente = df.loc[df['Medidor [W]'] == valor_cercano['Medidor [W]']]
    array = [fila_correspondiente['Sound system'].values[0],
                 fila_correspondiente['TV'].values[0],
                 fila_correspondiente['Play'].values[0],
                 fila_correspondiente['Oven'].values[0],
                 fila_correspondiente['Computer'].values[0],
                 fila_correspondiente['Clothes Iron'].values[0],
                 fila_correspondiente['Clothes washer'].values[0],
                 fila_correspondiente['Refrigerator'].values[0],]
    return array


# Función para generar los valores dentro de un rango
def generar_valores_rango(rango):
    valores = []
    inicio, fin = map(float, rango.split('-'))
    paso = 0.5  # El paso para los decimales
    valor_actual = inicio  # Inicializar valor_actual con el valor inicial del rango
    while valor_actual <= fin:
        valores.append(round(valor_actual, 1))  # Redondear al decimal más cercano
        valor_actual += paso
    return valores


def aletoriedad(array):
    i = random.randint(0,len(array)-1)
    j = random.randint(0,len(array[i])-1)
    return array[i][j]
# Entrada
def combinaciones(wats,sound_system,tv,play,oven,computer,clothes_iron,clothes_wash,refrigerator):
    wats = float(wats)
    combinaciones = []
    for i in range(2000):
        combinaciones.append([aletoriedad(sound_system),aletoriedad(tv),aletoriedad(play),aletoriedad(oven),aletoriedad(computer),aletoriedad(clothes_iron),aletoriedad(clothes_wash),aletoriedad(refrigerator)])

    combinaciones_validas= []
    for i in combinaciones:
        total = sum(i)
        if total >= wats - 60 and total <= wats:
                combinaciones_validas.append(i)
    return np.array(combinaciones_validas)

def calcular_distancia(arr1,arr2):
    return np.linalg.norm(arr1-arr2)