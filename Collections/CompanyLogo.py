'''
https://www.hackerrank.com/challenges/most-commons
'''
from collections import Counter


if __name__ == '__main__':
    s = input()
    
    [print(*i) for i in Counter(sorted(s)).most_common(3)]