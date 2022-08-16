import pandas as pd

df_books=pd.read_csv("C:\\Users\\Esteban\\Documents\\Programacion\\Platzi\\Python\\CursoPy\\NumPy_Pandas\\bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv", 
sep=",", header=0)

#Crear una funcion cualquiera

def two_times(value):
    return value * 2


print(df_books['User Rating'].apply(two_times))

#ejemplo, apolicar funcion tipo lambda
print(df_books['User Rating'].apply(lambda x: x* 3))

#aplica una funcion lambda a todo el df, multiplica por dos el valor de User Rating si el genero es fiction, sino lo deja igual
#Lo aplica al axis=1, es decir columnas
print(df_books.apply(lambda x: x['User Rating'] * 2 if x['Genre'] == 'Fiction' else x['User Rating'], axis = 1))