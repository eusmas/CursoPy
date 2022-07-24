#crear una lista con los primeros 100 numeros naturales al cuadrado
def run():
    my_list=[]
    my_list2=[]

    for i in range(1,101):
        my_list.append(i**2)
    print("Lista 1", my_list,"\n")

#crear una lista con los primeros 100 numeros naturales al cuadrado que no sean divisibles entre 3
    for i in range(1,101):
        if i %3 != 0:
            my_list2.append(i**2)
    print("Lista 2", my_list2,"\n")

#_____FORMA CORTA DE GENERAR EL MISMO CODIGO ANTERIOR, PERO CON "LIST COMPREHENSIONS"

#[element for element in iterable if condition]
#element= representa cada elemento que se va a poner en la nueva lista
#for element in iterable= ciclo a partir del cual se extraeran elementos de otra lista o cualquier iterable
#if condition= condicion opcional para filtrar los elementos del ciclo
    my_list3=[i**2 for i in range(1,101) if i%3 != 0]

    print("Lista 3", my_list3,"\n")


    #crear una lista de todos los multiplos de 4, que son multiplos de 6 y 9, hasta 5 digitos
    my_list4=[i for i in range(1,10001) if i%4 == 0 and i%6== 0 and i%9 == 0]

    print("Lista 4", my_list4)    
    

if __name__ == "__main__":
    run()