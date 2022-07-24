#FOR es para listas, tuplas y diccionarios
from ast import Break


dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"] #Se define una lista, para ejecutar los siguientes ejemplos

#Ejemplo de for con listas, Recorre el vectos lista con la variable x automaticamente 
for x in dias:
    print(x)
    print("_____")

#Ejemplo de for con Break, con el break lo que se hace es detener el ciclo for
for y in dias:
    print(y)
    if y=="Viernes":
        break
print("_____")

#Ejemplo de for con excepcion, aca no incluye la variable que detiene el ciclo 
for z in dias:
    if z=="Viernes":
        break
    print(z)
print("_____")


#Ejemplo de fos de repeticion
numero=5

for x in range(numero):
    print("Hola")
else:
    print("Fin ejemplo")
