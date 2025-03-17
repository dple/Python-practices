def funcA(lst, n, s):
    n += 1
    lst.append(4)
    s += " World"
    print(lst)
    print(n)
    print(s)


x = 3
str = "Hello"
lstt = [1, 2, 3]

funcA(lstt, x, str)
print(lstt)
print(x)
print(str)
x += 1
str += " World"
print(x)
print(str)

"""
d1 = [10, 20, 30, 40, 50]
d2 = [1, 2, 3, 4, 5]


subtracted = list()
for d1, d2 in zip(d1, d2):
    item = d1 -d2
    subtracted.append(item)

print(subtracted)
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(list(x))
#list = ['a', 'b', 'c', 'd', 'e']
#print(list[10:] )
list = ['a', 'b', 'c'] * -3
print(list)
data = [2, 3, 9]
temp = [[x for x in[data]] for x in range(3)]
print (temp)
"""