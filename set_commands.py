def commands(st, m):
    for _ in range(m):
        cmd = input().split()
        if cmd[0] == 'pop':
            st.pop()
        elif cmd == 'remove':
            st.remove(int(cmd[1]))
        else:
            st.discard(int(cmd[1]))

    print(sum(st))
if __name__ == '__main__':
    n = int(input().strip())            # number of set elements
    s = set(map(int, input().split()))
    m = int(input().strip())            # number of commands

    for _ in range(m):
        cmd, *values = input().split()
        values = tuple(map(int, values))
        command = f"s.{cmd}{values}"
        eval(command)

    print(sum(s))
    """
    Input sample
    9
    1 2 3 4 5 6 7 8 9
    10
    pop
    remove 9
    discard 9
    discard 8
    remove 7
    pop 
    discard 6
    remove 5
    pop 
    discard 5

    """