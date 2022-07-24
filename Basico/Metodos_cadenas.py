#nombre=input("Cual es tu nombre: ")

nombre=" abcdefghijk "

#Pone todo en mayuscula
nombre=nombre.upper()
print(nombre)

#pone la primera en mayuscula
nombre=nombre.capitalize()
print(nombre)

#elimina los espacios vacios al inicio y al final
nombre=nombre.strip()
print(nombre)

#pone todo en minuscula
nombre=nombre.lower()
print(nombre)

#reemplaza un caracter por otro
nombre=nombre.replace("n", "m")
print(nombre)

#se puede obtener un caeracter especifico de la cadena
print(nombre[3])

#devuelve la longitud del string
print(len(nombre))

#Slices
#Entrega el numero de caracteres a partir de un indice
print(nombre[0:3])

#Entrega el numero de caracteres a partir de un indice en pasos de 2
print(nombre[0:7:2])

#Una forma de invertir la cadena del string, para que quede al reves
print(nombre[::-1])