#Como usar tuplas
nombres= ("carlos", "marco", "luz", "luis")
numeros=(1,2,2,4,5)
valor=(True, False, True)
combinada= ("marco", 2, 4, True, False)

print(nombres)
print(numeros)
print(valor)
print(combinada)

print(len(nombres))

#Acceder a elementos de una tupla.

print(nombres[2])
print(combinada[3])
print(combinada[1:4])

#Actualizar una tupla.
x=list(combinada)
print(x)
x[1]="oscar"
combinada=tuple(x)
print(x)
print(combinada)

#Desempaquetar una tupla
(uno, dos, tres, cuatro, cinco)=combinada
print(cuatro)


#Metodos de una tupla count, index
print(numeros.count(2))
print(numeros.index(4))
