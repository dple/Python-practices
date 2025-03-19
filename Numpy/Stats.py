from numpy import array, mean, var, std

arr = []
n, m = map(int, input().split())

for _ in range(n):
    arr.append([*map(int, input().split())])
arr = array(arr)

print(mean(arr, axis=1))
print(var(arr, axis=0))
print(round(std(arr), 11))

'''
Sample Input

2 2
1 2
3 4
Sample Output

[ 1.5  3.5]
[ 1.  1.]
1.11803398875
'''