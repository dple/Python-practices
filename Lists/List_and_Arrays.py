'''
List1 = [3, 4, 7, 2]
List2 = [5, 2, 7, 1]


m = min(len(List1), len(List2))
'''

k = int(input("Enter the number of elements: "))
List1 = []
List2 = []
for i in range(k):
    ele = int(input())
    List1.append(ele)
    ele = int(input())
    List2.append(ele)

UltimateList = []

for i in range(k):
    UltimateList.append(List1[i] + List2[i])

print(UltimateList)

'''
if len(List_1) >= len(List_2):
    for i in range(0, len(List_2)):
        UltimateList.append(int(List_2[i]) + int(List_1[i]))

    print(UltimateList)

if len(List_2) > len(List_1):
    for i in range(0, len(List_1)):
        UltimateList.append(int(List_2[i]) + int(List_1[i]))

    print(UltimateList)
'''
'''
if len(List_2) == len(List_1):
    for i in range(0, len(List_1)):
        UltimateList.append(int(List_2[i]) + int(List_1[i]))

    print(UltimateList)
'''