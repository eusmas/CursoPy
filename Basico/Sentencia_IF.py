
print("Introducir un numero")
numero=int(input())

#Al poner varios if,el software evalua todas las posibilidades, serian 3 condiciones a evaluar
if numero > 0:
    print("El numero es positivo")
if numero <=0:
    print("El numero es negativo")
if numero % 2 == 0:
    print("El numero es Par")


#Al poner varios elif, el software evalua todo como si fuera una sola condicion
print("Introducir otro numero")
numero2=int(input())

if numero2 > 0:
    print("El numero es positivo")
elif numero2 <=0:
    print("El numero es negativo")
elif numero2 % 2 == 0:
    print("El numero es Par")


#evalua la variable en difernetes valores, el que tiene "_" es el por defecto en caso de no cuimplir ninguno de los anteriores 
def http_error(status):
    match status:
        case 400:
            return "Solicitud incorrecta"
        case 404:
            return "No encontrado"
        case 418:
            return "Soy una tetera"
        case _:
            return "Algo anda mal en internet"


