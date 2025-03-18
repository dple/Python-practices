"""
https://www.hackerrank.com/challenges/no-idea
"""
if __name__ == '__main__':
    n, m = input().split()
    lis = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    
    happiness = 0
    for i in lis:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
        
    print(happiness)
