n = int(input())

for _ in range(n):
    a, b = input().split()
    
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as ze:
        print("Error Code:", ze)
    except ValueError as ve:
        print("Error Code:", ve)