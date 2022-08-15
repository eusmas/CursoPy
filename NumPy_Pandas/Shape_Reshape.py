#import pandas as pn

from random import random
import numpy as np

lista=np.random.randint(1,10,(3,2))

#shape entrega cuantas filas y columnas tiene un arreglo
print(lista.shape)

#reshape cambia la forma establecida de un array
print(lista.reshape(1,6))


#reshape por defecto reordena los datos segun el orden por filas que tenga el original, pero esto se puede cambiar con las siguientes opciones
porfila=lista.reshape(1,6)
print(porfila)

porfila2=np.reshape(lista,(1,6),"C")
print(porfila2)

porColumna=np.reshape(lista,(1,6),"F")
print(porColumna)

#El optimizado lo hace segun el computador, no es controlable
porOptimizado=np.reshape(lista,(1,6),"A")
print(porOptimizado)