'''
https://www.hackerrank.com/challenges/np-dot-and-cross
'''
from numpy import array, dot 

n = int(input())

A = array([list(map(int, input().strip().split())) for _ in range(n)])
B = array([list(map(int, input().strip().split())) for _ in range(n)])

print(dot(A, B))

'''
Sample Input

2
1 2
3 4
1 2
3 4
Sample Output

[[ 7 10]
 [15 22]]
'''