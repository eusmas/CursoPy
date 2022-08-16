import pandas as pd
import numpy as np

#crear un diccionario
dict = {'Col1':[1,2,3,np.nan],
'Col2':[4, np.nan,6,7],
'Col3':['a','b','c', None]}

print("diccionario  ", dict)

#crear el data frame a partir del diccionario anterior
df= pd.DataFrame(dict)
print("df  ", df)

#Identifica los valores nulos
print("df  ", df.isnull())
print("df  ", df.isnull()*1)


#Llenar los valores nulos
print("df  ", df.fillna("Missing"))

#Llena los valores nulos con una interpolacion de los datos
print("df  ", df.interpolate())

#eliminar todos los nulos
print("df  ", df.dropna())

