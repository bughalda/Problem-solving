"""
Given five positive integers, find the minimum and maximum values that can be calculated by 
summing exactly four of the five integers. Then print the respective minimum and maximum 
values as a single line of two space-separated long integers.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    minimo = float('inf')
    maximo = float('-inf')
    totalsum = 0 
    
    
    for i in arr:
        minimo = min(minimo,i)
        maximo = max(maximo,i)
        totalsum+= i
        
    maxSum = totalsum - minimo
    minSum = totalsum - maximo
    
    print(minSum,maxSum)
           

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
