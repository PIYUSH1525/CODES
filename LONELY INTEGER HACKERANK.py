# Given an array of integers, where all elements but one occur twice, find the unique element.
#
# Example
#
# The unique element is .
#
# Function Description
#
# Complete the lonelyinteger function in the editor below.
#
# lonelyinteger has the following parameter(s):
#
# int a[n]: an array of integers
# Returns
#
# int: the element that occurs only once
# Input Format
#
# The first line contains a single integer, , the number of integers in the array.
# The second line contains  space-separated integers that describe the values in .
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here useing hashset
    hashset = {}
    for i in a:
        if i in hashset:
            hashset[i] += 1
        else:
            hashset[i] = 1
    for num, count in hashset.items():
        if count == 1:
            return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
