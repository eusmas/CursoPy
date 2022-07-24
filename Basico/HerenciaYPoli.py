#Herencia y polimorfismo

#La herencia consiste en utilizar metodos de otra clase "padre" sin necesidad de volverlos a declarar en la clase "hijo"
class padre:
    def __init__(self, numero):
        self.num=numero

    def mensaje1(self):
        print("Hola buenos dias")
    def mensaje2(self):
        print("Hola buenas tardes")
    def mensaje3(self):
        print("Hola buenas noches")


class hijo(padre):
    def __init__(self, numero): #el metodo init es del padre, la siguiente linea de codigo se crea automaticamente para evitar que queden dos metodos iguales
        super().__init__(numero)

    def mensaje4(self):
        print("Como has estado")
        print(self.num+10)
    def mensaje5(self):
        print("Como va la vida")
    def mensaje6(self):
        print("Hasta otra oportunidad")


ejemplo=hijo(13)

ejemplo.mensaje1()
ejemplo.mensaje2()
ejemplo.mensaje3()
ejemplo.mensaje4()
ejemplo.mensaje5()
ejemplo.mensaje6()


