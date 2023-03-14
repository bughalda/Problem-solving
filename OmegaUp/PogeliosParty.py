"""
Description
Pogelio is having a party tomorrow and is going to give pizza for dinner. 
Pogelio is a very righteous person, so he wants everyone to receive the same amount of pizza slices. 
He ordered pizzas from a company, but there was an accident and not all of them are complete. 
As you are good with problems, he asked you to help him. 
He wants to know the maximum amount of his friends he can invite.

Input
In the first line, two integers, and ,the number of pizzas he received and the number of friends he has.
In the second line, integers, the slices that each box contains.

Output
A single integer, the maximum amount of friends he can invite, so that Pogelio and his friends eat the same amount of slices.

"""



[n,k]=[int(x) for x in input().split(' ')]
arreglo=[int(x) for x in input().split(' ')]

slices = sum(arreglo)
friends= int(slices/(k+1))


while(k>0) and (slices % (k+1)!=0):
    k-=1
    friends= int(slices/(k+1))

if k == 0 or n == 0:
    print(0)
else:
    print(k)
