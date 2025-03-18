from collections import Counter

if __name__ == '__main__':
    # Print the element that appear the least in a list of elements
    print(Counter(input().split()).most_common()[-1][0])

    """
    sample input 
    1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
    sample output
    8
    """