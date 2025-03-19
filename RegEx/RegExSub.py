'''
https://www.hackerrank.com/challenges/re-sub-regex-substitution
'''

import re
N = int(input())
text = "\n".join(input() for _ in range(N))
print(re.sub(r'(?<=\s)&&(?=\s)', 'and', re.sub(r'(?<=\s)\|\|(?=\s)', 'or', text)))