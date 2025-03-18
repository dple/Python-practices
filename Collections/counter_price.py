from collections import Counter

X, c = int(input().strip()), Counter(input().split())
N = int(input())

total_price = 0
for i in range(N):
    size, p = input().split()
    if c[size] > 0:
        c[size] -= 1
        total_price += int(p)

print(total_price)

"""
Get the total price of shoes sold
Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200
Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned = 55 + 45 + 40 + 60 = 200
"""