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
#print(matriz[matriz%3==1])



#_____________________________

# #asi se puede crear un array con un tipo de dato preestablecido
# arr2=np.array([1,2,3,4,5,6,7,8,9], dtype="float64")
# print(arr2.dtype)
# print(arr2)

# #de esta forma se puede cambiar el tipo de dato de un array ya creado
# arr2=np.array([1,2,3,4,5,6,7,8,9])
# arr2=arr2.astype(np.float64)
# print(arr2.dtype)

# arr2=np.array([1,2,3,4,5,6,7,8,9])
# arr2=arr2.astype(np.bool8)
# print(arr2.dtype)
# print(arr2)

# arr2=np.array([1,2,3,4,5,6,7,8,9])
# arr2=arr2.astype(np.str_)
# print(arr2.dtype)
# print(arr2)

# arr2=np.array([1,2,3,4,5,6,7,8,9])
# arr2=arr2.astype(np.int8)
# print(arr2.dtype)
# print(arr2)

#_______________________________________
#Dimensiones

#elemento de 0 dimensiones, es un unico valor
scalar=np.array(42)
print(scalar)
print(scalar.ndim)

#elemento de 1 dimension, es un vector
vector=np.array([1,2,3])
print(vector)
print(vector.ndim)

#elemento de 2 dimensiones, es una matriz
matriz=np.array([[1,2,3], [4,5,6]])
print(matriz)
print(matriz.ndim)

#elemento de X dimensiones, se denomina Tensor
tensor=np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(tensor)
print(tensor.ndim)

#se define un vector con 10 dimensiones
vectorDos=np.array([1,2,3],ndmin=10)
print(vectorDos)
print(vectorDos.ndim)

#para agregar una nueva dimensiones a algo ya creado
#en Python, el 0 son las filas, el 1 son las columnas
expand=np.expand_dims(np.array([1,2,3]), axis=0)

print(expand)
print(expand.ndim)


#eliminar dimensiones que no se estan usando
vectorTres=np.squeeze(vectorDos)
print(vectorTres, vectorTres.ndim)


#Definir un tensor con 5 dimensiones, luego agregar una, borrar 2
tensorEus=np.array([[[1,2,3],[2,3,4]],[[3,4,5],[3,4,5]]], ndmin=5)
print(tensorEus, tensorEus.ndim)

tensorEus=np.expand_dims(tensorEus, axis=0)
print(tensorEus, tensorEus.ndim)

tensorEus=np.squeeze(tensorEus)
print(tensorEus, tensorEus.ndim)