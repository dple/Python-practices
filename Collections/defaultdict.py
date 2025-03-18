"""
Problem:
In this challenge, you will be given  integers, n and m. There are n words, which might repeat, in word group A.
There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Sample Input:
5 2
a
a
b
a
b
a
b

Sample Output:
1 2 4
3 5

Explanation:
'a' appeared  times in positions 1, 2 and 4.
'b' appeared  times in positions 3 and 5.
"""
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
d['A'] = [input() for _ in range(n)]
d['B'] = [input() for _ in range(m)]

for x in d['B']:
    if x in d['A']:
        for i, v in enumerate(d['A']):
            if x == v:
                print(i + 1, end=' ')
        print()
    else:
        print(-1)

