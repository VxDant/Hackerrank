#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):

    output_list = []

    for i in range(0,len(queries)):
        new_numbers = []

        query = queries[i]

        start_index = query[0]

        emd_index = query[-2]



        if start_index == emd_index:
            new_numbers.append(numbers[start_index-1])

        else:
            for i in range(start_index-1,emd_index):
                new_numbers.append(numbers[i])


        sum1 = sum(new_numbers)

        counter = 0

        for i in new_numbers:
            if i == 0:
                counter +=1


        sum1 = (query[len(query)-1] * counter) + sum1

        output_list.append(sum1)


    return output_list

if __name__ == '__main__':


    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = findSum(numbers, queries)

    print(result)
