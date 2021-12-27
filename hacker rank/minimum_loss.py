#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price,m=-5000000000000000):  # heart of the code. 
    # Write your code here
    """                                                 # alternate implementation with n^2 complexity.
    m=min(price[1]-price[0],price[0]-price[1])
    for i in range(len(price)-1):
        for j in range(i+1,len(price)):
            if price[j]>price[i]:
                continue
            k = price[j]-price[i]
            if k>m:
                m=k"""
    if len(price)<=1:
        return m
    L=[]
    R=[]
    e=price[0]
    for i in range(1,len(price)):
        if price[i]<e:
            L.append(price[i])
            k=price[i]-e
            if k>m:
                m=k
            print(m)
        else:
            R.append(price[i])
    m=minimumLoss(L,m)
    m=minimumLoss(R,m)
    return m
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = abs(minimumLoss(price))

    fptr.write(str(result) + '\n')

    fptr.close()
