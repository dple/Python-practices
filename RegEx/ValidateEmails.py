'''
Validate email addresses
https://www.hackerrank.com/challenges/validating-named-email-addresses
'''
import email.utils
import re 

n = int(input())
pattern = r'^[a-z](\w|-|\.)*@[a-z]+\.[a-z]{1,3}$'

for _ in range(n):
    s = input()
    parse = email.utils.parseaddr(s)    
    if re.match(r'[^\W_\,][.\w-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$', parse[1]) != None:
        print(s)
   