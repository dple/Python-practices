def funcA(l):
    l.append([2, 3])
    l[0] = 4



def funcB():
    l = [0, 0]

    funcA(l)
    print(l)


if __name__ == '__main__':
    funcB()


