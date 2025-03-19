import re

pat1 = r'[A-Z]{2,}'
pat2 = r'[0-9]{3,}'
pat3 = r'^[a-zA-Z0-9]{1,}$'
pat4 = r'([a-zA-Z0-9])\1+'

for _ in range(int(input())):
    a = input()
    a = sorted(a)
    a = ''.join(a)

    b1 = re.search(pat1, a) is not None
    b2 = re.search(pat2, a) is not None
    b3 = re.match(pat3, a)  is not None
    b4 = re.search(pat4, a) is None
    b5 = len(a) == 10
    
    print('Valid' if all([b1, b2, b3, b4, b5]) else 'Invalid')