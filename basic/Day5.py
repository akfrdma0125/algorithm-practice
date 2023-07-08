# 루프 이용

def divide_same_word(s1, s2):
    if set(s1) != set(s2):
        return 0

    for i in range(len(s1)):
        if s1[i:] + s1[:i] == s2 or s1[-i:] + s1[:-i] == s2:
            return i

    return 0


# w.o. loop b 문자열 2배
divide_same_word2 = lambda a, b: (b * 2).find(a)
