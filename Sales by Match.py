#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    c = Counter(ar)
    sum1 = 0

    for i in c.values():
        sum1 += i // 2

    return sum1


if __name__ == '__main__':
    

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
