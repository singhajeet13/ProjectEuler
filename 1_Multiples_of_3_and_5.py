import sys
import numpy as np

def muplipleOrNot(num):
    if((num % 15 ==0) | (num % 5 ==0) | (num % 3 ==0)):
        return 1
    else:
        return 0

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    