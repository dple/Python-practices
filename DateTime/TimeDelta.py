'''
https://www.hackerrank.com/challenges/python-time-delta/
'''
import os
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    d1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    d2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    diff = d2 - d1
    return str(int(abs(diff.total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
