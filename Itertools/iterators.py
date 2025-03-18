'''
https://www.hackerrank.com/challenges/iterables-and-iterators
'''
from itertools import combinations

N, string, K = int(input()), input().split(), int(input())
res = [i for i in combinations(string, K)]
print(len([i for i in res if 'a' in i])/len(res))
