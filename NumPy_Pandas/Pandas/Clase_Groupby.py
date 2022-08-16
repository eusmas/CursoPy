import pandas as pd

df_books=pd.read_csv("C:\\Users\\Esteban\\Documents\\Programacion\\Platzi\\Python\\CursoPy\\NumPy_Pandas\\bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv", 
sep=",", header=0)


#agrupar por autor el .count es para que me cuenta la cantidad de registros que hay por cada autor
#se pueden usar complementos como .max .min .avg ...etc
print(df_books.groupby("Author").count())

print(df_books.groupby("Author").sum())


#El resultado es un nuevo DF cuyos indices son los autores (para el ejemplo), esto implica que se pueden usar los nombres para busquedas
now=df_books.groupby("Author").sum().loc["William Davis"]
print(now)

#Si no se quiere que el autor sea el index, se hace lo siguiente.
print(df_books.groupby("Author").sum().reset_index())

#agrupar por autor el minimo y el maximo
print(df_books.groupby("Author").agg(["min", "max"]))


#agrupar por autor el minimo y el maximo
#print(df_books.groupby("Author").agg{"Reviews":["min", "max"]})

#Volver a ver la clase 18, no entendi el ultimo tema