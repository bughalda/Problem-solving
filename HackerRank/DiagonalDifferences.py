#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
"""

def diagonalDifference(arr):
    i = 0
    j = len(arr[0])-1
    sumDiagLeft = 0
    sumDiagRight = 0
    
    for i in range(len(arr)):
        sumDiagLeft+= arr[i][i]
        sumDiagRight+= arr[i][j]
        j-=1
    return abs(sumDiagLeft-sumDiagRight)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
