if __name__ == '__main__':
    # Creating a list comprehension by using conditionals in list comprehension
    pow2 = [2 ** x for x in range(10) if x > 5]
    print(pow2)
    # Get a list of even numbers
    even = [x for x in range(20) if x % 2 == 0]
    print(even)
    tens = [x for x in range(200) if x%2 == 0 if x%5 == 0]
    print(tens)

    # Using if ... else with list
    lst = [[i, "Even"] if i%2 == 0 else [i, "Odd"] for i in range(20)]
    print(lst)

    # Get a list by using lambda function
    ch_list = list(map(lambda c: c, 'human'))
    print(ch_list)
    # print without commas or bracket
    print(*ch_list)
    print(' '.join(map(str, ch_list)).center(20, '-'))

    # Get list from a string
    ch_list = list("human")
    print(ch_list)
    print(''.join(ch_list))

    ch_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
    # Test the membership
    print('a' in ch_list)
    print('o' in ch_list)
    # Get the top element
    print(ch_list.pop())