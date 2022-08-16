import pandas as pd
import numpy as np

#Se crean dos diccionarios
dic1={"A":["A0","A1","A2","A3"], "B":["B0","B1","B2","B3"], "C":["C0","C1","C2","C3"], "D":["D0","D1","D2","D3"]}
dic2={"A":["A4","A5","A6","A7"], "B":["B4","B5","B6","B7"], "C":["C4","C5","C6","C7"], "D":["D4","D5","D6","D7"]}

#Se convierten en DataFrames
df1=pd.DataFrame(dic1)
df2=pd.DataFrame(dic2)


#concat

#Concatenar un df con otro, agregando el segundo al final del primero
#con ignore_index=True se crean nuevos indice, sino se pone, se duplican los index 
print(pd.concat([df1,df2],ignore_index=True))

#Si se pone el axis=1, se concatena en las columnas
print(pd.concat([df1,df2],axis=1))


#Merge

#Ver imagen guardada para entender el resultado
izq = pd.DataFrame({'key' : ['k0', 'k1', 'k2','k3'],
 'A' : ['A0', 'A1', 'A2','A3'],
'B': ['B0', 'B1', 'B2','B3']})

der = pd.DataFrame({'key' : ['k0', 'k1', 'k2','k3'],
 'C' : ['C0', 'C1', 'C2','C3'],
'D': ['D0', 'D1', 'D2','D3']})

print(izq.merge(der))


#join

#Pivot

#Ver clases

