'''
https://www.hackerrank.com/challenges/find-angle
'''
from math import atan, degrees
AB = int(input())
BC = int(input())

angleC = atan(AB/BC)
print((round(degrees(angleC))),chr(176),sep='')