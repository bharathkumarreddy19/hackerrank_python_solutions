import math
import os
import random
import re
import sys

# Complete the powerSum function below.
n = 1
def powerSum(X, N):
    for i in range(1,X):
        i = pow(i,2) + pow(1,2)
        i += 1
        if i == X:
            print(i)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
