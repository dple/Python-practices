def print_formatted(number):
    # your code goes here
    d = number
    bin_d = len(bin(d)[2:])
    for x in range(1, d + 1):
        # For built-in math functions: oct, hex, bin, get values from the 3rd position to remove prefix 0o, 0x, 0b
        print(repr(x).rjust(bin_d), oct(x)[:2].rjust(bin_d), hex(x).upper()[:2].rjust(bin_d), bin(x)[:2].rjust(bin_d))


def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))
    print('\n'.join(L[::-1] + L[1:]))


def rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    L = []
    for i in range(size):
        s = '-'.join(alphabet[i:size])
        L.append((s[:0:-1] + s).center(4 * size - 3, '-'))
    print('\n'.join(L[:0:-1] + L))


def minion_game(w):
    stuart = 0
    kevin = 0
    vowel = "aeiouAEIOU"
    for i in range(len(w)):
        if w[i] in vowel:
            kevin += len(w[i:])
        else:
            stuart += len(w[i:])
    if stuart > kevin:
        print("Stuart " + str(stuart))
    elif stuart < kevin:
        print("Kevin " + str(kevin))
    else:
        print("Draw")


def capitalize_name(s):
    for w in s.split():
        s = s.replace(w, w.capitalize())
    return s


if __name__ == '__main__':
    n = int(input().strip())
    print_formatted(n)
    #word = input()
    #minion_game(word)
    # m = int(input())
    # rangoli(m)
    # str = input()

    # print(capitalize_name(str))
