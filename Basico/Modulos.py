#Modulos
def suma(x,y):
    resultado=x+y
    return resultado, x, y


def factor(numero):
    if numero==1:
        return 1
    else:
        return (numero*factor(numero-1))


def numeroposi(x):
    if x > 0:
        return "Tu Numero es Positivo"
    elif x < 0:
        return "Tu Numero es Negativo"
    elif x == 0:
        return "Tu Numero es cero"


def ciclo(x):
    while x <= 10:
        print(x)
        x+=1