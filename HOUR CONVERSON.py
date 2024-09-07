# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
#
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
#
# Example
#
#
# Return '12:01:00'.
#
#
# Return '00:01:00'.
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return "00" + s[2:-2]
        else:
            return s[:-2]
    else:
        h = int(s[:2])
        if h < 12:
            h += 12
        return str(h) + s[2:-2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
