#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findPositions' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER s
#  4. 2D_INTEGER_ARRAY queries
#




def findPositions(a, b, s, queries):
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    a = int(first_multiple_input[0])

    b = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    results = findPositions(a, b, s, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in results]))
    fptr.write('\n')

    fptr.close()