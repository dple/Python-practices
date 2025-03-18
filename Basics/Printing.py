if __name__ == '__main__':
    arr = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Print the entire list
    print(arr)

    # Print a list slicing
    print(arr[3:])

    # Remove commas and brackets
    # Option 1: using method join on map
    print(' '.join(map(str, arr)))
    # Option 2: using asterisk (*)
    print(*arr)

    # print a float in python
    pi = 3.142659
    # Using %-fprmatting
    print("%.2f" %pi)
    # Using str.format
    print("{:.2f}".format(pi))
    # Using f-strings
    print(f"{pi:.2f}")