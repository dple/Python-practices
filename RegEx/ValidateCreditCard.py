'''
https://www.hackerrank.com/challenges/validating-credit-card-number
'''
import re
pat1 = r'^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$'
pat2 = r'(\d)\1{3,}'

for i in range(int(input())):
    a = input()
    a2 = re.sub(r'-',"", a)
    
    b1 = re.match(pat1, a) is not None
    b2 = re.search(pat2, a2)   is None
    
    print('Valid' if all([b1, b2]) else 'Invalid')