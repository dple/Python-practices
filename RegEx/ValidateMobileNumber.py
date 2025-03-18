'''
A valid mobile number is a ten digit number starting with a 7, 8 or 9.
https://www.hackerrank.com/challenges/validating-the-phone-number
'''
import re 

for _ in range(int(input())):
    s = input().strip()
    print('YES' if re.match(r'^[789]\d{9}', s) and len(s) == 10 else 'NO')