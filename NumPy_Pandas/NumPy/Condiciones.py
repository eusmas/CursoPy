import numpy as np

arr=np.arange(1,11)

print("Arreglo  ", arr)

#devuelve un array de falses y trues donde se cumpla la condicion
indices_cond=arr>5

print("Indices de condicion  ", indices_cond)
#al poner un array de false y true dentro de otro array de valores, devuelve solo lo que esta en true
print("Indices de condicion dentro del array ", arr[indices_cond])

#De esta forma se obtiene el mismo resultado de forma mas directa
print("Indices directos  ", arr[(arr>5)])

#Se pueden poner condicionales dentro de la busqueda de indice
print("Indices directos 2 ", arr[(arr>5) & (arr<9)])



