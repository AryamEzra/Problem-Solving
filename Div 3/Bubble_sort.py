#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    numswaps = 0
    for i in range(n):
        num_of_swaps = 0
        for j in range(n-1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j+1], a[j]
                num_of_swaps += 1
            
        if num_of_swaps == 0:
            break
        else:
            numswaps += num_of_swaps
    print("Array is sorted in " + str(int(numswaps)) + " swaps.")
    print("First Element: " + str(int(a[0])))
    print("Last Element: " + str(int(a[n-1])))
      
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
    
    
