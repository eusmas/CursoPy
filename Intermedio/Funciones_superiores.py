from functools import reduce


my_list=[1,2,3,4,5,6,9,19,21]


#funcion superior "filter"
#crea otra lista solo con numeros impares
odd=list(filter(lambda x: x%2 !=0, my_list))
print(odd)

#funcion superior "map"
#convierte la lista en otra pero con los numeros al cuadrado
squares=list(map(lambda x: x**2, my_list))
print(squares)


#funcion superior "reduce"
#multiplicar todos los numeros de una lista
my_list2=[2,2,2,2,2]
all_multiplied=reduce(lambda x,y: x*y, my_list2)
print(all_multiplied)