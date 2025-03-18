'''
https://www.hackerrank.com/challenges/piling-up
'''
t = int(input())
res = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left, right = 0, n - 1
    top_stack = float('inf')
    while left < right:
        if arr[left] > arr[right]:
            next_top_stack = arr[left]
            left += 1
        else:
            next_top_stack = arr[right]
            right -= 1
        
        if next_top_stack > top_stack:
            ans = 'No'
            break
        else:
            top_stack = next_top_stack
            ans = 'Yes'
    res.append(ans)
    
for x in res:
    print(x)
