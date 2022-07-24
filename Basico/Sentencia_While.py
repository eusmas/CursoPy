#Uso del While en Python
numero =1


#Repeticion de numeros
while numero <= 10:
    print(numero)
    numero+=1
print("_____")
numero =1

#Repeticion de numeros con BREAK
while numero <= 10:
    print(numero)
    if numero == 6:
        break
    numero+=1
print("_____")
numero =0

#Repeticion de numeros con CONTINUE
while numero <10:
    numero+=1
    if numero==6:
        continue
    print(numero)
print("_____")
numero =0


#Suma de numetos naturales
numeros=int(input("Introducir un numero entero "))

resul=0
contro=1

while contro<=numeros:
    resul+= contro
    contro+=1
print("La suma de numeros naturales es: ",resul)


