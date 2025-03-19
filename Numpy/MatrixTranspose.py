'''
https://www.hackerrank.com/challenges/np-transpose-and-flatten
'''
import numpy

n, m = map(int, input().strip().split())

matrix = [list(map(int, input().strip().split())) for _ in range(n)]
np_matrix = numpy.array(matrix)
print(numpy.transpose(np_matrix))
print(np_matrix.flatten())

'''
Sample Input

2 2
1 2
3 4
Sample Output

[[1 3]
 [2 4]]
[1 2 3 4]
'''