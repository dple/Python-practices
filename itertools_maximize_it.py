from itertools import product

k, m = map(int, input().split())

res = [[int(j)**2 for j in input().split()[1:]] for i in range(k)]
print(max([sum(i)%m for i in product(*res)]))