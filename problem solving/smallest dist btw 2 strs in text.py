'''
@Author: rishi
'''


def solve(text, word0, word1):
    text = text.split(" ")
    word0_loc = []
    word1_loc = []
    for i in range(len(text)):
        if text[i] == word0:
            word0_loc.append(i)
        if text[i] == word1:
            word1_loc.append(i)

    print(word0_loc)
    print(word1_loc)
    main_dist = 9987654321
    for i in word0_loc:
        for j in word1_loc:
            if abs(i - j) < main_dist:
                main_dist = abs(i - j) - 1
    return main_dist

text = "a a b a b b"
word0 = "a"
word1 = "b"
print(solve(text, word0, word1))