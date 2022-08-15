import numpy as np

lista=np.random.randint(1,20,10)
matriz=lista.reshape(2,5)

print("lista  ", lista)
print("matriz  ", matriz)


#Maximo numero del arreglo
print("maximo   ",matriz.max())

#Maximo numero por filas
print("maximo filas   ", matriz.max(1))

#Maximo numero por columnas
print("maximo columnas   ",matriz.max(0))

#Devuelve el indice donde esta el Maximo numero del arreglo
print("Indice maximo   ",matriz.argmax())

#Devuelve el indice donde esta el Maximo numero por filas
print("Indice maximo filas   ", matriz.argmax(1))

#Devuelve el indice donde esta el Maximo numero por columnas
print("Indice maximo columnas   ",matriz.argmax(0))

#Minimo numero del arreglo, funciona todo igual que el max, con todas las combinaciones con arg
print("Minimo ", matriz.min())

#entrega la diferencia entre el valor mas grande y el mas peque, si se pone un numero en el parentesis hace el calculo por eje 0:Columnas 1:Filas
print("Pico a pico ", matriz.ptp())

#Devuelve el percentil del arreglo
print("Percentil ", np.percentile(matriz,50))

#Ordena de menor a mayor
lista.sort()
print("Sort ", lista)

#Entrega la mediana
print("Mediana ", np.median(lista))

#desviacion estandar
print("Desviacion estandar ", np.std(matriz))

#varianza
print("Varianza ", np.var(matriz))

#Entrega la media
print("Media ", np.mean(matriz))

#concatenar
a=np.array([[1,2],[3,4]])
b=np.array([5,6])
#se expande la dimension de b para poder concatenar con a
b=np.expand_dims(b,axis=0)

print("Concatenar por columnna   ", np.concatenate((a,b),axis=0))
print("Concatenar por fila   ", np.concatenate((a,b.T),axis=1)) #la b.T es para transponer la matriz

