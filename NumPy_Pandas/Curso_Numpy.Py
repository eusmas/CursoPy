#import pandas as pn

import numpy as np

lista= [1,2,3,4,5,6,7,8,9]
#print(lista)

arr=np.array(lista)
#print(type(arr))

matriz=[[1,2,3], [4,5,6], [7,8,9]]
matriz=np.array(matriz)
#print(matriz)

#Cuando se llama un index en un array, me devuelve un numero
#print(arr[5])

#Cuando se llama un index en un array, de esta forma me devuelve una serie de numeros dados por el parentesis 
#print(arr[2:9])

#Cuando se llama un index en un array, Si no se pone uno de los valores, si no se pone el primero, toma desde el inicio. Si no se pone el final, toma hasta el final.
#print(arr[:6])
#print(arr[6:])

#Cuando se llama un index en un array, el tercer digito, sirve para obtener el paso entre los datos.
#print(arr[::2])

#Cuando se llama un index en un array, con los digitos en negativo, empieza a llamar desde el final.
#print(arr[3::])
#print(arr[::-1])


#_________________

#Cuando se llama un index en una matriz, me devuelve una fila
#print(matriz[0])

#Cuando se llama un index en una matriz, de esta forma me devuelve un numero exacto, x,y en la matriz
#print(matriz[0,2])

#Cuando se llama un index en una matriz, de esta forma me devuelve un numero de filas 
#print(matriz[0:2:])

#Cuando se llama un index en una matriz, de esta forma me un regresa rango de finales
#print(matriz[0:2:])

#Cuando se llama un index en una matriz, de esta forma me regresa un rango de filas con un paso determinado
#print(matriz[0:3:2])

#Cuando se llama un index en una matriz, regresa el dato desde la fila 1, columna 0 en pasos de 2
#print(matriz[1:,0:2])

#Forma de traer una sola columna de la matriz
#print(matriz[0:,0:1])


#__________________
#Se pueden llamar valores segun alguna condicion, por ejemplo, llamar los numeros mayores a 5
print(matriz[matriz%3==1])



