# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#
# Example
#
# The minimum sum is  and the maximum sum is . The function prints
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def miniMaxSum(arr):
    # Write your code here
    minn = 0
    maxx = 0
    arr.sort()
    for i in range(0, 4):
        minn += arr[i]
    arr.reverse()
    for i in range(0, 4):
        maxx += arr[i]

    print(minn, maxx)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
