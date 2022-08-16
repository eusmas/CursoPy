import pandas as pd
import numpy as np

df_books=pd.read_csv("C:\\Users\\Esteban\\Documents\\Programacion\\Platzi\\Python\\CursoPy\\NumPy_Pandas\\bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv", 
sep=",", header=0)

print(df_books.head(2))

#para filtrar por una condicion, se asigna primero a una variable y luego esta variable es la que se imprime dentro del rango
Condicion_año=df_books["Year"] > 2016
print(df_books[Condicion_año])

Condicion_genre=df_books["Genre"] == "Fiction"
print(df_books[Condicion_genre])

#concatenar condiciones
print(df_books[Condicion_genre & Condicion_año])

#con el ~ es la negacion
print(df_books[~Condicion_año])

