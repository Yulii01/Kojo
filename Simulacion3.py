#T = tiempo transcurrido
# t_A = Tiempo de llegada del cliente
# t_f = Tiempo de salida del cliente
# N = cantidad de clientes en la cola
# entradas,salidas = {} : almacenar 

import cocineroExtra as clt
import Generacion as gnr
import matplotlib.pyplot as plt


def cociero(Tiempo,Sist,entr,Arribo,cant):
    T = Tiempo 
    t_A = Arribo
    Sistema = clt.Sistema()

    Sistema.t_s1= Sist.t_s1 
    Sistema.t_s2 = Sist.t_s2 
    Sistema.t_s3 = 999999999
    Sistema.primero = Sist.primero
    Sistema.segundo = Sist.segundo
    Sistema.cant_de_pendiente = Sist.cant_de_pendiente
    Sistema.cola=Sist.cola
    n = cant        
    Cierre = (21 - 10) * 60
    


    while(clt.Pico(T)) :  # Simulacion General
        
        if(min(t_A,Sistema.t_s1,Sistema.t_s2,Sistema.t_s3) == t_A and t_A <= Cierre):
            n = n +1  # llega 1 nuevo
            T = t_A
            t_A = T + gnr.Tiempo_Arribo(T)
            cliente = clt.Cliente(T,n)

            entr.append(cliente)

            Sistema.anadir(cliente , T)


        if(min(t_A,Sistema.t_s1,Sistema.t_s2,Sistema.t_s3) == Sistema.t_s1 and Sistema.t_s1 <= Cierre):
            T = Sistema.t_s1
            Sistema.Primero_Saca(entr,T)



# Generar caso salida de 2
        if(min(t_A,Sistema.t_s1,Sistema.t_s2,Sistema.t_s3) == Sistema.t_s2 and Sistema.t_s2 <= Cierre):
            T = Sistema.t_s2
            
            Sistema.Segundo_Saca(entr,T)
        
        if(min(t_A,Sistema.t_s1,Sistema.t_s2,Sistema.t_s3) == Sistema.t_s3 and Sistema.t_s3 <= Cierre):
            T = Sistema.t_s3
            
            
            Sistema.TerceroSaca(entr,T)


        if (t_A >= Cierre and min(Sistema.t_s1,Sistema.t_s2,Sistema.t_s3) == Sistema.t_s1 and Sistema.cant_de_pendiente > 0 ):
            T = Sistema.t_s1
            Sistema.Primero_Saca(entr,T)

    
     
        if (t_A >= Cierre and min (Sistema.t_s1,Sistema.t_s2,Sistema.t_s3) == Sistema.t_s2 and Sistema.cant_de_pendiente > 0  ):
            T = Sistema.t_s2

            Sistema.Segundo_Saca(entr,T)
         
        if (t_A >= Cierre and min (Sistema.t_s1,Sistema.t_s2,Sistema.t_s3) == Sistema.t_s3 and Sistema.cant_de_pendiente > 0  ):
            T = Sistema.t_s3
           
            

            Sistema.TerceroSaca(entr,T)
         
        
        
    

    
    return T,Sistema,t_A,n    

