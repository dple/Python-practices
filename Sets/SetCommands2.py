def test_getattr():
    """
    getattr will return the method/function/attribues associated with specific object,
    in this case it's getting the methods from set object a then i'm calling the method with given input
    """
    input()
    a = set(map(int, input().split()))

    for _ in range(int(input())):
        name, *_ = input().split()
        getattr(a, name)(set(map(int, input().split())))

    print(sum(a))

if __name__ == '__main__':

    m = int(input().strip())
    A = set(map(int, input().split()))
    N = int(input())

    for _ in range(N):
        cmd, n = input().split()
        lis = set(map(int, input().split()))
        print(cmd, lis)
        s = f"A.{cmd}({lis})"
        eval(s)

    print(sum(A))