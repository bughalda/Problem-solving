"""
Dadas las coordenadas de una casilla en un tablero de ajedrez de 8x8, determinar el color de dicha casilla.
"""

[letter,number]=[x for x in input().split(' ')]
number = int(number)

c1 = ['a','c','e','g']
c2 = ['b','d','f','h']

if(letter in c1):
    if(number % 2 == 0):
        print("BLANCO")
    else:
        print("NEGRO")
elif(number % 2 == 0):
    print("NEGRO")
else:
    print("BLANCO")

