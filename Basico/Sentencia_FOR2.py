#ejemplo de platzi

# ejemplo de como recorrer un for en un rango numerico
for x in range(1,10):
    print(x)
    
#ejemplo de como no imprimire los numeros pares de un range, cuando se cumple la condicion del if, se salta ese paso del for
for contador in range(1,100):
    if contador %2 != 0:
        continue
    print(contador)

#cuando el contador llega a 53, el break termina el ciclo for
for i in range(0,100):
    print(i)
    if i==53:
        break


for i in range(0,100):
    if i==53:
        break
    print(i)