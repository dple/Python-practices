'''
https://www.hackerrank.com/challenges/word-order
'''
n = int(input().strip())
d = {}

for i in range(n):
    k = input()
    d[k] = 1 + d.get(k, 0)
    
print(len(d))
print(*d.values())