from typing import List
import Generacion as gnr

class Cliente ():

    def __init__(self,t_A,N_A):
        self.tipo = gnr.Tipo_Cliente()
        self.llegada = t_A
        self.partida = 0
        self.numero = N_A
        self.Tiempo_Elaboracion = 0


    def Salida (self,T_d):
        self.partida = T_d

    
def Pico(T):
    return 90 <= T <=210 or 420<= T <= 540

class Sistema () :
    def __init__(self) :
        self.cant_de_pendiente = 0
        self.primero = 0
        self.segundo = 0
        self.tercero=0
        self.t_s1 = 999999
        self.t_s2 = 999999
        self.t_s3 = 99999
        self.cola = []
        
    def anadir (self,Cliente :Cliente , Tiempo):
                
        if(self.primero == 0):
            self.primero = Cliente.numero
            elaborar =  gnr.Generar_elaboracion(Cliente)
            Cliente.Tiempo_Elaboracion = elaborar
            self.t_s1 = Tiempo + elaborar
            

        elif (self.segundo == 0):
            self.segundo = Cliente.numero
            elaborar =  gnr.Generar_elaboracion(Cliente)
            Cliente.Tiempo_Elaboracion=elaborar
            self.t_s2 = Tiempo + elaborar
              
        elif (self.tercero == 0 ):
            self.tercero = Cliente.numero
            elaborar =  gnr.Generar_elaboracion(Cliente)
            Cliente.Tiempo_Elaboracion=elaborar
            self.t_s3 = Tiempo + elaborar
        else:
            self.cola.append(Cliente.numero)
        self.cant_de_pendiente = self.cant_de_pendiente + 1           


    def Primero_Saca (self,lista , Tiempo):
        lista[self.primero].partida= Tiempo
        if (self.cant_de_pendiente <=3):
            self.primero=0
            self.t_s1= 999999999

        else :
            self. primero = self.cola.pop(0)
            elaborar= gnr.Generar_elaboracion(lista[self.primero])
            self.t_s1 = Tiempo + elaborar
            lista[self.primero].Tiempo_Elaboracion=elaborar
            

        self.cant_de_pendiente = self.cant_de_pendiente - 1

    def Segundo_Saca (self,lista , Tiempo):
        lista[self.segundo].partida = Tiempo
        if (self.cant_de_pendiente <=3):
            self.segundo=0
            self.t_s2= 999999999

        else :
            self. segundo = self.cola.pop(0)
            elaborar= gnr.Generar_elaboracion(lista[self.segundo])
            self.t_s2 = Tiempo + elaborar
            lista[self.segundo].Tiempo_Elaboracion=elaborar
            

        self.cant_de_pendiente = self.cant_de_pendiente - 1
        

    def TerceroSaca (self,lista , Tiempo):
        lista[self.tercero].partida = Tiempo
        if (self.cant_de_pendiente <=3):
            self.tercero=0
            self.t_s3= 999999999

        else :
            self.tercero = self.cola.pop(0)
            elaborar= gnr.Generar_elaboracion(lista[self.tercero])
            self.t_s3 = Tiempo + elaborar
            lista[self.tercero].Tiempo_Elaboracion=elaborar
            

        self.cant_de_pendiente = self.cant_de_pendiente - 1


