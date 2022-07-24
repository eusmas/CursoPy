# Diccionarios en python
nombres={1:"marco", 2:"juan", 3:"lola", 4: True, 5:False, 6:"juan"} 
print(nombres)

tupla={"nombre":"marco", "edad":25, "tup":("marco", 2,4,"gorge") }
print(tupla)

lista={"nombre":"marco", "edad":25, "list":["marco", 2,4,"gorge"] }
print(lista)

print(len(nombres))
print(len(lista))

#Acceder a elementos Keys(), Values(), items()

print(nombres[2])

x=nombres[2]
print(x)

print(nombres.keys()) #Muestra las claves que tiene el diccionario
print(nombres.values()) #Muestra los valores almacenados
print(nombres.items()) #??? no entendi #devuelve la clave con el valor almacenado


#Cambiar elemento update()

nombres[2]="Esteban" 
print(nombres)

nombres.update({2:"Carla"})
print(nombres)


#agregar elemento

nombres.update({7:"Lili"})
print(nombres)


#eliminar elemento pop(), popitem(), del, clear()

nombres.pop(3)
print(nombres)

nombres.popitem()
print(nombres)

del nombres[1]
print(nombres)


nombres.clear()
print(nombres)


