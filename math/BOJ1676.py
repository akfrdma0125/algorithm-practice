import math

num = math.factorial(int(input()))
print(num)
result = 0
while num%10 == 0:
    print(num%10)
    result += 1
    num //= 10
print(result)