from django.shortcuts import render
from .custom_def.Limpiezadedatos import *
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Desagregacion
import random
import numpy as np
from django.http import JsonResponse
from desagregacionCargas.models import *


# Create your views here.
@csrf_exempt
def index(request):
  wats = [random.randint(120,2000) for i in range(60)]
  date = [4.20+i for i in range(60)]
  # Electrodomesticos con sus rangos de gastos
  sound_system = [generar_valores_rango("0-5"),generar_valores_rango("10-40")]
  tv = [generar_valores_rango("0-5"),generar_valores_rango("60-80")]
  play = [generar_valores_rango("0-3"),generar_valores_rango("20-40")]
  oven = [generar_valores_rango("0-21"),generar_valores_rango("1360-1628")]
  computer = [generar_valores_rango("0-3"),generar_valores_rango("35-43")]
  clothes_iron = [generar_valores_rango("0-15"),generar_valores_rango("800-1100")]
  clothes_wash = [generar_valores_rango("0-15"),generar_valores_rango("150-200"),generar_valores_rango("350-500")]
  refrigerator = [generar_valores_rango("0-8"),generar_valores_rango("120-160"),generar_valores_rango("300-450")]

  ruta = os.path.join(settings.BASE_DIR ,'desagregacionCargas','custom_def','sources','ordenada.csv')
  inicial = obtener_valor_inicial(wats[0],ruta)
  desagregacion = Desagregacion()
  desagregacion.hora = date[0]
  desagregacion.wats = wats[0]
  desagregacion.estado = 1 if wats[0]>10 else 0
  desagregacion.sound_system = inicial[0]
  desagregacion.tv = inicial[1]
  desagregacion.play = inicial[2]
  desagregacion.oven = inicial[3]
  desagregacion.computer = inicial[4]
  desagregacion.clothes_iron = inicial[5]
  desagregacion.clothes_wash = inicial[6]
  desagregacion.refrigerator = inicial[7]
  desagregacion.save()
  for j,i in enumerate(wats[1:]):

      combinacion = combinaciones(i,sound_system,tv,play,oven,computer,clothes_iron,clothes_wash,refrigerator)
      inicial = np.array(inicial)
      distancias = [calcular_distancia(inicial,h) for h in combinacion]
      indice_mas_cercano = np.argmin(distancias)
      inicial = combinacion[indice_mas_cercano].astype('float')

      desagregacion = Desagregacion()
      desagregacion.hora = date[j+1]
      desagregacion.wats = wats[j+1]
      desagregacion.estado = 1 if wats[j+1]>10 else 0
      desagregacion.sound_system = inicial[0]
      desagregacion.tv = inicial[1]
      desagregacion.play = inicial[2]
      desagregacion.oven = inicial[3]
      desagregacion.computer = inicial[4]
      desagregacion.clothes_iron = inicial[5]
      desagregacion.clothes_wash = inicial[6]
      desagregacion.refrigerator = inicial[7]
      desagregacion.save()
  return render(request,'index.html',{})
