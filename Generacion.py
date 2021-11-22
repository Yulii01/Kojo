import random as r
import numpy as np

def Tipo_Cliente () :
    return r.randint(0,1)
    

def Generar_elaboracion (Cliente) :
    if(Cliente.tipo == 0):
        return round((3 + (5-3)*r.random()),3)
    return round((5 + (8-5)*r.random()),3)

def Tiempo_Arribo (T) :
    if(90 <= T <=210 or 420<= T <= 540):    # Hora Pico
        return round( (-(1/0.5)* np.log(r.random())),3)

    return round( (-(1/0.1)* np.log(r.random())) , 3)


def Elaboracion_Sushi ():
   return r.randint(10,20)
