def getGCD(a, b):
    if a % b == 0:
        return b
    return getGCD(b, a % b)


print(getGCD(192, 162))
