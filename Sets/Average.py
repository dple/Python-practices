# Give a list of plants' heights. Print the average of the distinct heights
def average(array):
    # Convert array to set to remove repeated items
    plants = set(array)
    return sum(plants)/len(plants)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)