#crear un diccionario con llaves de 100 numeros natuarales y significado del valor al cubo
def run():
    my_dict={}
    my_dict2={}

    for i in range(1,101):
        my_dict.update({i:i**3})
 
    print("Diccionario 1", my_dict,"\n")

 #crear una diccionario solo con los numeros que no sean divisibles en 3
    for i in range(1,101):
        if i %3 != 0:
            my_dict2.update({i:i**3})

    print("Diccionario 2", my_dict2,"\n")
    
 #crear una diccionario solo con los numeros que no sean divisibles en 3, pero con comprehension
    my_dict3={i:i**3 for i in range(1, 101) if i%3 !=0}
            
    print("Diccionario 3", my_dict3,"\n")

#crear un diccionario cuyas llaves sean los 1000 numeros naturales y el valor sea la raiz cuadrada

    my_dict4={i:i**0.5 for i in range(1, 1001) if True}
            
    print("Diccionario 4", my_dict4,"\n")
    

if __name__ == "__main__":
    run()