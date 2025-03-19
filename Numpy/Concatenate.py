'''
Concatenate two matrices n x p and m x p along axis 0
https://www.hackerrank.com/challenges/np-concatenate
'''
import numpy

n, m, p = map(int, input().strip().split())

arr1 = [list(map(int, input().strip().split())) for _ in range(n)]
arr2 = [list(map(int, input().strip().split())) for _ in range(m)]

np_arr1 = numpy.array(arr1)
np_arr2 = numpy.array(arr2)

print(numpy.concatenate((np_arr1, np_arr2), axis = 0))

'''
Sample Input

4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
Sample Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
'''