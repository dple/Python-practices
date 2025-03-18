'''
Given a string, find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.
https://www.hackerrank.com/challenges/re-group-groups
'''
import re 
m = re.search(r"([a-zA-Z0-9])\1", input())
print(m and m.group(1) or -1)