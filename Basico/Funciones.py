#funciones en python
def mifuncion():
    print("Hola mundo")

mifuncion()


def suma(x,y):
    resultado=x+y
    return resultado, x, y

sumando=suma(5,3)
print(sumando)

sum1=int(input("Primer numero para sumar: "))
sum2=int(input("Segundo numero para sumar: "))
print (suma(sum1,sum2))

#Recursividad
def factor(numero):
    if numero==1:
        return 1
    else:
        return (numero*factor(numero-1))

num3=int(input("Numero para factorial: "))
print("Factorial es: ")
print(factor(num3))

#Uso de if
def numeroposi(x):
    if x > 0:
        return "Tu Numero es Positivo"
    elif x < 0:
        return "Tu Numero es Negativo"
    elif x == 0:
        return "Tu Numero es cero"

num4=int(input("Numero para estudiar: "))
print(numeroposi(num4))


#Uso de WHile

def ciclo(x):
    while x <= 10:
        print(x)
        x+=1

numero=1
ciclo(numero)
