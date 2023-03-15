#!/bin/python3

import math
import os
import random
import re
import sys
        
def timeConversion(s):
    selector = s[8:10]
    hora = int(s[0:2])
    
    if selector == 'AM':
        if hora == 12:
            return "00" + s[2:8]
        else:
            return s[0:8]
    else:
        if hora == 12:
            return s[0:8]
        else:
            hora += 12
            return str(hora) + s[2:8]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
