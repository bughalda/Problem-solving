"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though 
answers with absolute error of up to  are acceptable.
Example
[1,1,0,-1,-1]
There are  elements, two positive, two negative and one zero. Their ratios are 0.4,0.4 and 0.2.
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    cont = [0,0,0]
    n = len(arr)
    
    for i in arr:
        if i > 0:
            cont[0] += 1
        elif i < 0:
            cont[1] += 1
        else:
            cont[2] += 1

    for i in cont:
        print(i/n)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
