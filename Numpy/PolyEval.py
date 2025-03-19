'''
Evaluate a polynomial using Numpy
https://www.hackerrank.com/challenges/np-polynomials
'''
import numpy as np 

print(np.polyval(list(map(float, input().split())), float(input())))

'''
Sample Input

1.1 2 3
0
Sample Output

3.0
'''
