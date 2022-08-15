import numpy as np

#forma clasica de crear un array
lista=list (range(0,10))

#forma de crear array con numpy
lista2=np.arange(0,10,2)

#zeros sirve para crear un array lleno de ceros
lista3=np.zeros((10,10))

#zeros sirve para crear un array lleno de unos
lista4=np.ones((10,10))

#crea una lista con la cantidad de datos conocida, se da un inicio, un final y la cantidad de datos
lista5=np.linspace(0,10,2)

#Crear una matriz con la diagonal en 1
lista6=np.eye(3)

#crea un numero aleatorio entre 0 y 1
numero=np.random.rand()

#crea un array de numeros aleatorios
lista7=np.random.rand(4)

#crea una matriz de numeros aleatorios
lista8=np.random.rand(4,4)

#crea un numero aleatorio entre los dos numeros escritos
lista9=np.random.randint(1,4)

#crea una matriz con los numeros aleatorio entre los dos numeros escritos
lista10=np.random.randint(1,10, (4,4))

print(lista10)
