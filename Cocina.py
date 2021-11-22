#T = tiempo transcurrido
# t_A = Tiempo de llegada del cliente
# t_f = Tiempo de salida del cliente
# N = cantidad de clientes en la cola
# entradas,salidas = {} : almacenar 

import cliente as clt
import Generacion as gnr
import matplotlib.pyplot as plt
import Simulacion3 as Sim
from cocineroExtra import Pico , Sistema


def Kojo(tipo):
    T = t_A = t_s1 = t_s2 = t_F = n = n_1 = n_2 = sis =  n_S1 = n_S2 =0     
    t_A = gnr.Tiempo_Arribo(T)
    t_s1 = t_s2 = 9999999
    t_s3 =9999999
    entr = []
    entr.append(0)
    Tercero =0
    salid = {}
    Cierre = (21 - 10) * 60
    Sistema = clt.Sistema()
    xy=1


    while(True) :  # Simulacion General
        if(tipo):
            if(Pico(T)):
                xy=0
                T,Sist,t_A,n = Sim.cociero(T,Sistema,entr,t_A,n)
                Sistema.t_s1= Sist.t_s1 
                Sistema.t_s2 = Sist.t_s2 
            
                Sistema.primero = Sist.primero
                Sistema.segundo = Sist.segundo
                tercero = Sist.tercero
                t_s3 = Sist.t_s3
                Sistema.cant_de_pendiente = Sist.cant_de_pendiente
                if(Sist.tercero != 0):
                    entr[Sist.tercero].partida = Sist.t_s3
                    Sistema.cant_de_pendiente = Sistema.cant_de_pendiente -1 
                Sistema.cola = Sist.cola

        if(min(t_A,Sistema.t_s1,Sistema.t_s2) == t_A and t_A <= Cierre):
            n = n +1  # llega 1 nuevo
            T = t_A
            t_A = T + gnr.Tiempo_Arribo(T)
            cliente = clt.Cliente(T,n)
            entr.append(cliente)

            Sistema.anadir(cliente , T)
        

        if(min(t_A,Sistema.t_s1,Sistema.t_s2) == Sistema.t_s1 and Sistema.t_s1 <= Cierre):
            T = Sistema.t_s1
            n_S1 = n_S1 +1 
            salid[Sistema.primero]= T
            Sistema.Primero_Saca(entr,T)



# Generar caso salida de 2
        if(min(t_A,Sistema.t_s1,Sistema.t_s2) == Sistema.t_s2 and Sistema.t_s2 <= Cierre):
            T = Sistema.t_s2
            salid[Sistema.segundo]= T
            
            Sistema.Segundo_Saca(entr,T)

        if (t_A >= Cierre and min(Sistema.t_s1,Sistema.t_s2) == Sistema.t_s1 and Sistema.cant_de_pendiente > 0 ):
            T = Sistema.t_s1
            n_S1 = n_S1 +1 
            salid[Sistema.primero]= T
                        
            Sistema.Primero_Saca(entr,T)

        if(min(t_A,Sistema.t_s1,Sistema.t_s2,t_s3) == Sistema.t_s3 and Sistema.t_s3 <= Cierre):
            T = t_s3
            
            entr[tercero].partida = T
            t_s3 = 99999999
            tercero = 0
            

        if (t_A >= Cierre and min (Sistema.t_s1,Sistema.t_s2,Sistema.t_s3) == Sistema.t_s3 and Sistema.cant_de_pendiente > 0  ):
            T = t_s3
           
            
            entr[tercero].partida = T
            t_s3 = 99999999
            tercero = 0  
     
        if (t_A >= Cierre and min (Sistema.t_s1,Sistema.t_s2) == Sistema.t_s2 and Sistema.cant_de_pendiente > 0  ):
            T = Sistema.t_s2
            n_S1 = n_S1 +1 
            salid[Sistema.segundo]= T

            Sistema.Segundo_Saca(entr,T)
        
        if (t_A >= Cierre  and Sistema.cant_de_pendiente == 0):
            promedio = 0
            x=[]
            y=[]
            for i in range(1,len(entr)):
                if(round( (entr[i].partida - entr[i].llegada - entr[i].Tiempo_Elaboracion), 3) >5):
                    promedio = promedio + 1
                x.append(entr[i].partida - entr[i].llegada )
                y.append(entr[i].partida)    
            print( "El % de los que esperan mas de 5 min es " ,promedio / (len(entr)-1 )* 100)
            
            plt.plot(x,y)
            plt.show()
            break 

Kojo(True)  
Kojo(False)
            
