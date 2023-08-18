import math
from sys import stdin

# 소수 구하기

def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(n) + 1)):
        if arr[i]:
            j = 2

            while (i * j) <= n:
                arr[i * j] = False
                j += 1

    return arr


arr = is_prime_num(100000)
primes = []

for i in range(len(arr)):
    if arr[i]:
        primes.append(i)

n = int(stdin.readline())

for _ in range(n):
    i = 0
    cnt = 0
    number = int(stdin.readline())
    while number > 1:
        if number % primes[i] != 0:
            if cnt > 0:
                print(f'{primes[i]} {cnt}')
            cnt = 0
            i += 1
            continue
        number //= primes[i]
        cnt += 1
    print(f'{primes[i]} {cnt}')
