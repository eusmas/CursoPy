import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

df_books=pd.read_csv("C:\\Users\\Esteban\\Documents\\Programacion\\Platzi\\Python\\CursoPy\\NumPy_Pandas\\bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv", 
sep=",", header=0)

print(df_books.head(2))

#entregar informacion del data frame
print(df_books.info())

#entregar informacion estadistica de las columnas numericas
print(df_books.describe())


#entrega los ultimos x reguistros, es como el Head, pero los ultimos
print(df_books.tail(2))

#entrega cuanta memoria consume cada columna
print(df_books.memory_usage(deep=True))

#cuenta la cantidad de veces que se repiten los valores en la columna buscada
print(df_books["Author"].value_counts())

#borrar elementos duplicados
#Ejemplo, se agrega la fila cero nuevamente
df_books=df_books.append(df_books.iloc[0])
print(df_books)
#con drop_duplicate se borra la fila duplicada
print(df_books.drop_duplicates())

#ordenar valores de forma ascendente
print(df_books.sort_values("Year"))

#ordenar valores de forma descendente
print(df_books.sort_values("Year", ascending=False))