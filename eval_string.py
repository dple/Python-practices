if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        cmd, *values = input().split()
        values = tuple(map(int, values))
        print(cmd, values)
        if cmd == "print":
            s = f"{cmd}(lst)"
        else:
            s = f"lst.{cmd}{values}"
        eval(s)
        """
        elif cmd == "pop":
            s = f"lst.{cmd}()"
        elif cmd == "reverse":
            s = f"lst.{cmd}()"
        elif not values:
            
        """


    #print(lst)
    """
    Input Sample
    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print

    """