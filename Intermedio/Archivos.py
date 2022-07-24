def read():
    numbers=[]

    with open("./archivos/numbers.txt","r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names=["Asd", "Miguel", "Pepe", "Esteban", "María"]
    with open("./archivos/names.txt","a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()

if __name__=="__main__":
    run()



# Modos de Apertura 

# r -> Solo lectura
# r+ -> Lectura y escritura
# w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# a -> Añadido (agregar contenido). Crea el archivo si éste no existe
# a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.


# with open(<ruta>, <modo_apertura>) as <nombre>

# dentro del codigo el archivo se llama como <nombre>