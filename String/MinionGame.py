'''
https://www.hackerrank.com/challenges/the-minion-game
'''
def minion_game(w):
    # your code goes here
    stuart = 0
    kevin = 0
    vowel = "AEIOU"
    for i in range(len(w)):
        if w[i] in vowel:
            kevin += len(w[i:])
        else:
            stuart += len(w[i:])
    if stuart > kevin:
        print("Stuart " + str(stuart))
    elif stuart < kevin:
        print("Kevin " + str(kevin))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)