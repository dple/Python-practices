'''
https://www.hackerrank.com/challenges/python-sort-sort/
'''

# Sort a 2D array based on the key from the kth column 
def sort2D(arr, k):
    sorted_arr = [arr[i][k] for i in range(n)]
    
    sorted_arr.sort()
    
    for x in sorted_arr:
        j = 0
        while arr[j][k] != x:
            j += 1
        print(*arr[j])
        arr.pop(j)

def sort2D_optimized(arr, k):
    # Using lambda function to get the key that will be used to sort
    arr.sort(key=lambda x: x[k])
    for i in range(len(arr)):
        print(*arr[i])


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())
    
    sort2D_optimized(arr, k)
        