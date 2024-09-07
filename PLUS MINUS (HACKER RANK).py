# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
#
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
#
# Example
#
# There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:
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
    arr.sort()
    min_count = 0
    max_count = 0
    zero_count = 0
    for i in range(0, len(arr)):
        if arr[i] == 0:
            zero_count += 1
        elif arr[i] > 0:
            max_count += 1
        elif arr[i] < 0:
            min_count += 1
    print(max_count / len(arr))
    print(min_count / len(arr))
    print(zero_count / len(arr))

    # Write your code here


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
