if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))

    lis = list(a.symmetric_difference(b))
    lis.sort()
    for x in lis:
        print(x)