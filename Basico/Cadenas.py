#Cadenas en python
nombre="marco {}"
edad=35

nombres="""marco
luis
rosa
carlos
"""


#Trabajar con una cadena
for x in nombre:
    print(x)
print(len(nombre))

print(nombres)

print(nombre*3)

#Cortar Cadenas
print(nombre[0:2])          #separar caracteres en una cadena


#Cadenas y sus metodos: upper, lower, replace, format
print(nombre.upper()) #pone todo en mayuscula

print(nombre.lower()) #pone todo en minuscula

print(nombre.replace("o","l"))          #reemplazar un caracter por otro

print(nombre.format(edad))
