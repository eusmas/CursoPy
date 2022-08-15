import numpy as np

arr=np.arange(0,11)

print("Arreglo  ", arr)

#El copy se utiliza para conservar intacto el arreglo original y no modificarlo con las diferentes funciones que se pueden aplicar
#Si no se hace con copy, al modificar el nuevo array, se modifica el original, asi funciona Pyhton y Numpy
arr_copia=arr.copy()
print("Copia del Arreglo  ", arr_copia)

#Para el ejemplo, en la copia se reemplazan todos los valores por 20, el arreglo original sigue intacto
arr_copia[:]=20
print("Copia del Arreglo  ", arr_copia)
print("Arreglo  ", arr)





