"""
Descripción
Los estudiantes del ITAM suelen comer en fondas ubicadas en las calles aledañas al ITAM. A Miguel le gusta pedir 
sopa de letras para entretenerse buscando su nombre entre las letras; saca las letras de la sopa tantas veces como 
sea posible para formar su nombre, y si no logra encontrar letras suficientes para formar su nombre aunque sea una 
vez, Miguel se enoja y golpea furiosamente la mesa.
Los amigos de Miguel quieren asegurarse de que éste no golpee la mesa cuando vayan a comer, así que les gustaría 
saber cuántas veces puede Miguel formar su nombre con una sopa de letras.
Todas las letras son minúsculas.

Entrada
Un string S que contiene todas letras que hay en la sopa.

Salida
El número de veces que Miguel pudo formar su nombre con las letras de la sopa.
"""

s = list(input())
nombre = list("miguel")

cont = 0
condicion  = True

while(condicion):
    i = 0
    while(i<len(nombre) and condicion):
        if(nombre[i] in s):
            s.remove(nombre[i])
        else:
            condicion = False
        i+=1
    if(i==len(nombre)):
        cont+=1

print(cont)
    
