# i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.
def get_factorial(n):
    num = 1
    result = 1
    while True:
        num *= result
        if num > n:
            break
        else:
            result += 1
    return result - 1


# 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.
def get_count_k(i, j, k):
    result = ''
    for no in range(i, j + 1):
        result += str(no)
    return result.count(str(k))
