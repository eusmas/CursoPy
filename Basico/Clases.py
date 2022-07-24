class miprimerclase:
    #atributos de instancia
    def __init__(self):
        print("Hola")
    #Metodos
    def mensaje1(self):
        print("Buenas tardes")
    def mensaje2(self):
        print("Adios")
               

mensaje=miprimerclase()
print(type(mensaje.mensaje1))

mensaje.mensaje1()
mensaje.mensaje2()

#----------------------------------


class clase2:
    def __init__(self, numero):
        self.numero=numero
    def comparar(self):
        if self.numero > 0:
            print("El numero es positivo")
        elif self.numero == 0:
            print("El numero es cero")
        elif self.numero < 0:
            print("El numero es negativo")
    def ciclo(self):
        while self.numero<=10:
            print(self.numero)
            self.numero +=1

        
ejemplo=clase2(0)
ejemplo.comparar()
ejemplo.ciclo()