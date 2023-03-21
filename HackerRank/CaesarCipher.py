#!/bin/python3

import math
import os
import random
import re
import sys

"""
  Julius Caesar protected his confidential information by encrypting it using a cipher.
  Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end
  of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation
  by 3, w, x, y and z would map to z, a, b and c.
  Complete the 'caesarCipher' function below.
  The function is expected to return a STRING.
  The function accepts following parameters:
  string s
  integer k
"""


def caesarCipher(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    result=[]
    
    while i < len(s):
        if s[i].lower() in alphabet:
            char = s[i].lower()
            index = (alphabet.index(char) + k) % len(alphabet)
            if s[i].isupper():
                result.append(alphabet[index].upper())
            else:
                result.append(alphabet[index])
        else:
            result.append(s[i])   
        i += 1
    
    return "".join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
