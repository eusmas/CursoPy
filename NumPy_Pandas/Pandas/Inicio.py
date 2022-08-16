import pandas as pd

#Las series son de una sola dimencion
#Los dataframe son de mas de 3 dimensiones

#Series
#creacion de una serie con los index conocidos
serie=pd.Series(["Esteban", "Lili", "Maria", "Olga"], index=[10,20,30,40])

print("Serie   ", serie)

#creacion de una serie con los index por default
serie2=pd.Series(["Esteban", "Lili", "Maria", "Olga"])
print("Serie2  ", serie2)

#Creacion de un diccionario
dic={1:"Navas", 7:"Mbappe", 10:"Neymar", 30:"Messi"}
print("Diccionario  ", dic)

#a seria se le pueden pasar datos para ser convertidos 
print("Diccionario como serie  ", pd.Series(dic))

#se puede acceder a la informacion segun su indice
print("Accediendo en una posicion  ", serie[20])
print("Accediendo en una posicion  ", serie2[3])
print("Accediendo en una posicion  ", serie2[0:2])



#DataFrames

#creacion del diccionario
dic2={"Jugador":["Navas","Mbappe","Neymar","Messi"], "Altura":[183, 170, 170, 165], "Goles": [2,200,200,150]}
print("Diccionario  ", dic2)
#se convierte en un dataframe y se asignan los index de forma conocida
dicdf=pd.DataFrame(dic2,index=[1,7,10,30])
print("Diccionario DF  ", dicdf)

#Se puede acceder a la informacion de un dataframe por columnas o filas
print("DF columnas  ", dicdf.columns)
print("DF filas  ", dicdf.index)
