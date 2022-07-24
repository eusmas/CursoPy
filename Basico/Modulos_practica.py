import Modulos


sumando=Modulos.suma(5,3)
print(sumando)

sum1=int(input("Primer numero para sumar: "))
sum2=int(input("Segundo numero para sumar: "))

print(Modulos.suma(sum1,sum2))


num3=int(input("Numero para factorial: "))
print("Factorial es: ")
print(Modulos.factor(num3))


num4=int(input("Numero para estudiar: "))
print(Modulos.numeroposi(num4))

numero=6
print("Los Numeros Son:   ")
Modulos.ciclo(numero)