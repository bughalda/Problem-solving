"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
S = '12:01:00PM'
Return '12:01:00'.
S='12:01:00AM'
Return '00:01:00'.

Function Description
Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
timeConversion has the following parameter(s):
string s: a time in  hour format
Returns
string: the time in  hour format
Input Format
A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints
All input times are valid
"""


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
