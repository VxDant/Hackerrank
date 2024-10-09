#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # bill = [3, 10, 2, 9]
    sum1 = sum(bill)
    sum1 = sum1 - bill[k]
    sum1 = sum1 / 2
    if sum1 == b:
        print("Bon Appetit")
    else:
        print(int(abs(sum1 - b)))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
