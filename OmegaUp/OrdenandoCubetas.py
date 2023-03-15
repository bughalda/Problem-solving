"""
Descripcion
Estabas trabajando en una tienda de juguetes, ese día llego una carga de pelotas de varios colores, tu jefe puso a tu mejor amigo 
a ordenarlas, su tarea era separarlas por colores para poder ofrecerlas a los clientes. Sin embargo 
sabe que tienen muchos clientes daltónicos, por eso mismo ordeno las pelotas de distintos colores por números, al terminar esta 
tarea recibió una llamada de emergencia, su hijo estaba por nacer, por lo que se tuvo que ir. Como no termino de ordenar las 
pelotas y sabiendo que su jefe es muy estricto decidiste ayudar a tu amigo a terminar su tarea,por suerte el había dejado algunas cubetas
para que se puedan separar las pelotas, el único detalle es que debes contar la cantidad de pelotas, para poder meterlo al inventario.

Problema
Tu tarea es sencilla, únicamente debes imprimir el número y la cantidad de pelotas que hay de ese tipo, si no hay ninguna 
de ese color, debes imprimir 0, el número de colores no excederá de 100.

Entrada
Se te dará un entero N
que representa la cantidad de pelotas que hay y un entero M
que representa el mayor número que puedes encontrar en las pelotas. En la siguiente línea se te dará 
N elementos, los cuales son las distintas pelotas con su distinto número.

Salida
Debes imprimir todas las cantidades de pelotas, de manera ascendente empezando desde el 1 hasta M
,debes imprimir el número de la pelota seguido por dos puntos y un espacio, posteriormente la cantidad de pelotas 
que hay de ese tipo. Por ejemplo si tenemos 3 pelotas del color 1 se debe imprimir de la siguiente manera 1: 3
"""

[n,m]=[int(x) for x in input().split(' ')]
pelotas=[int(x) for x in input().split(' ')]

for i in range(1,m+1):
    print(str(i)+": "+str(pelotas.count(i)))
