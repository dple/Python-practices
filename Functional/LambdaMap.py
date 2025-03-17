'''
https://www.hackerrank.com/challenges/map-and-lambda-expression
'''
cube = lambda x: x**3 

def fibonacci(n):
    # return a list of fibonacci numbers
    res = [0, 1] + [0]*(n - 2)
    
    for i in range(2, n):
        res[i] = res[i - 1] + res[i - 2]
    
    return res

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))