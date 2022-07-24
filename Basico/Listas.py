#listas
nombres= ["marco", "juan", "caro", "roberto", "rosa"]
numeros=[1,2,2,4,5]
varios= [1,5,4,"mari", "juan", True, False]

print(nombres)
print(numeros)
print(varios)

print(len(nombres))

#Acceder a elementos de una lista.

print(nombres[3])
print(varios[3])
print(varios[2:4])

#Actualizar una lista.
nombres[1]="Lola"
print(nombres)
numeros[3]=5
print(numeros)
varios[5]=False
print(varios)

#Metodos de una lista append(), remove()
numeros.append("Oscar")
print(numeros)
numeros.pop(0) #elimina el elemento que tenga en el indice
numeros.remove(5) #elimina el elemendo igual a
print(numeros)