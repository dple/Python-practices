from itertools import product
if __name__ == '__main__':
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    print(*list(product(A, B, C)))
