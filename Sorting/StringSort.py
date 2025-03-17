'''
https://www.hackerrank.com/challenges/ginorts
'''

def get_weight(c):
    if c.islower():
        return ord(c)
    if c.isupper():
        return ord(c) + 100
    c = int(c)
    if c % 2:
        return c + 200
    return c + 400

if __name__ == '__main__':
    s = input().strip()
    s = sorted(s, key = get_weight)
    print(''.join(c for c in s))