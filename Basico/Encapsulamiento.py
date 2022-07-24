#Encapsulamiento

class enca():
    def __init__(self):
        self.__numero=0
    def operacion(self):
        print(self.__numero+20)
    def resultado(self):
        return self.__numero

ejemplo=enca()

ejemplo.operacion()

ejemplo.numero=100 #aca se esta modificando un atributo de la clase, es decir, se tiene un atributo publico. Al ponerle doble guien bajo a la variable de la clase, lo vuelve privado, es decir, no se puede modificar




print(ejemplo.resultado())