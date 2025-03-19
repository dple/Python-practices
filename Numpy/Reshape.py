'''
https://www.hackerrank.com/challenges/np-shape-reshape
'''
import numpy

arr = list(map(int, input().strip().split()))
np_array = numpy.array(arr)
np_array.shape = (3, 3)
print(np_array)

'''
Sample Input

1 2 3 4 5 6 7 8 9
Sample Output

[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''