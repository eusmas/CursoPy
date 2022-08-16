import pandas as pd
import numpy as np

#sep=separador de los datos
#header= en cual fila estan los encabezados
df_books=pd.read_csv("C:\\Users\\Esteban\\Documents\\Programacion\\Platzi\\Python\\CursoPy\\NumPy_Pandas\\bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv", 
sep=",", header=0)

#mostrar el data frame
print(df_books)

#mostrar un segmento del df
print(df_books[0:4])

#filtrar por una sola columna
print(df_books["Name"])

#filtrar por miltiples columnas
print(df_books[["Name", "Author"]])

#filtrar por miltiples columnas y filas
#loc permite mostrar solo algunas filas
#df.loc[fila,columnas]
print(df_books.loc[0:4,["Name", "Author"]])

#para filtrar por condiciones, en este ejemplo, buscan e todas las filas de la columna author los que se llamen jj smith
print(df_books.loc[:,["Author"]]== "JJ Smith")


#Iloc filtra por indice
print(df_books.iloc[:,0:3])
print(df_books.iloc[1,3])

#ejemplo, filtra hasta la fila 2 y desde la fila 2
print(df_books.iloc[:2,2:])


#Eliminar columnas de un df
#Head(2) permite mostrar solo los dos primeros indices
#inplace=True, hace que el borrado se haga sobre el archivo y no solo en la salida de consola
#axis=0 son las filas, axis=1 son las columnas
#ejemplo, se borra la columna year
df_books.drop("Year", axis=1, inplace=True)

print(df_books.head(4))


#ejemplo, se borra la fila 2
df_books.drop(2, axis=0, inplace=True)
print(df_books.head(4))

#ejemplo, se borra las fila 5,6 y 7
df_books.drop([5,6,7], axis=0, inplace=True)
print(df_books.head(10))


#ejemplo, se borra rl rango del 10 al 15
df_books.drop(range(10,15), axis=0, inplace=True)
print(df_books.head(15))



#agregar columnas
#np.nan es simplmente para llenar la columnas de valores no numericos "nan"
df_books["Nueva Columna"]=np.nan
print(df_books.head(15))


#agregar filas
df_books.append(df_books)
print(df_books)