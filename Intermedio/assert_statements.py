#LO MISMO QUE DEBUGING PERO CON ASSSERT STATEMENTS
#si se cumple la condicion dentro del assert, continua el programa normal
#si la condicion no se cumple, detiene el cpdigo


def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors
    

def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric(), "Debes ingresar un numero"
    assert int(num)>0, "Debes ingresar un numero positivo"
    print(divisors(int(num)))
    print("Terminó mi programa")



if __name__ == '__main__':
    run()

