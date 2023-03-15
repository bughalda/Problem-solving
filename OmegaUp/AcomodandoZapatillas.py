"""
Descripción
Ayla es una niña que tiene demasiadas zapatillas y un día decidió acomodar cada una de ellas, mientras 
las acomodaba se dio cuenta que tenía un desorden y así que decidió re-ordenarlas y tirar a la basura 
todas las zapatillas que se habían quedado solas. Ayla tiene un montón de zapateros en donde tiene una 
infinidad de zapatillas.

Problema:
Realiza un programa que dadas la cantidad de zapatillas que tenía, y un identificador de cada zapatilla, 
decir de cuantas zapatillas se puede deshacer Ayla, es decir, todas las que han perdido su par. 
Dos zapatillas son del mismo par si tienen el mismo identificador.

Entrada
En la primer línea, un numero N con la cantidad de zapatillas que tiene Ayla. En la segunda línea, 
K números, el identificador de cada una de las zapatillas.

Salida
En la primera línea los identificadores de las zapatillas que puede tirar, en la segunda línea la 
cantidad de zapatillas que puede tirar y en la tercera línea la cantidad de zapatillas que Ayla se 
quedará, en caso de que Ayla haya encontrado todos los pares de las zapatillas debes imprimir :D 
en lugar de los identificadores.
"""


n=int(input())
k=[int(x) for x in input().split(' ')]

aux = [0] *(max(k)+1)
trash = 0
s = ""

for i in range(n):
    aux[k[i]]+=1

for i in range(len(aux)):
    if aux[i] != 0 and (aux[i] % 2) != 0:
        s += str(i) + " "
        trash += 1

if trash == 0:
    print(":D")
    print(0)
    print(n)
else:
    print(s)
    print(trash)
    print(n-trash)
