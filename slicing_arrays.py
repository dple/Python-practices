if __name__ == '__main__':
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # slicing with positive indexes
    print(alphabet[3:6])
    # slicing with negative indexes and index jump
    print(alphabet[-26::2])
    # slicing from the end of the list
    print(alphabet[:0:-2])
    print(alphabet[::-2])
    print('-'.join(alphabet[13:2:-1]).center(30, '-'))