from itertools import groupby

data = list(input().strip())
it = groupby(data)

for key, group in it:
    print(tuple([list(group), int(key)]), end=' ')