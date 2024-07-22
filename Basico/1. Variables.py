#llamar un codigo externo, en este caso se usa un codigo externo para 
#declarar todas las constantes, es una buena practica
import Constantes

#Ejemplo imprimir hola mundo
print('Hola Mundo')

#declarar un numero 
numeros=1234567890

#declarar un string
nombre="Esteban"

print(numeros)
print(nombre)

#se pueden declarar varias variables en una linea
nombre1, nombre2, ="Lili" , "Maria"
print(nombre1)
print(nombre2)

#se pueden declarar varias variables con un mismo valor
moto1=moto2="Pulsar"
print(moto1)
print(moto2)

#utilizar una variable que esta en otro archivo
print(Constantes.PI)

#ingresar un dato cualquiera por terminal
print("Escribir tu nombre: ")
nombre_entrada=input()
print(nombre_entrada, type(nombre_entrada))

#ingresar un dato entero por terminal
print("Escribir tu nombre: ")
numero_entrada=int(input())
print(numero_entrada, type(numero_entrada))