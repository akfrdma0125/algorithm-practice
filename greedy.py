import re
from functools import reduce


def get_big_number():
    N, M, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    numbers.sort(reverse=True)

    multiple = M // (K + 1)
    answer = (numbers[0] * K + numbers[1]) * multiple

    rest = M % (K + 1)
    if rest == 0:
        return answer
    return answer + numbers[0] * rest


def get_game_number():
    N, M = map(int, input().split())
    answer = 0
    for i in range(N):
        numbers = list(map(int, input().split()))
        number = min(numbers)
        # if answer < number:
        #     answer = number
        answer = max(answer, number)
    return answer


def set_number_one():
    n, k = map(int, input().split())
    answer = 0
    while n > 1:
        answer += n % k
        n //= k
        if n > 0:
            answer += 1
    return answer


# 백준 11399: ATM
def get_best_sequence():
    n = int(input())
    numbers = list(map(int, input().split()))

    # sort
    numbers.sort()

    # 합 구하기
    answer = [0]
    for number in numbers:
        answer.append(answer[-1] + number)

    return sum(answer)

# 백준 ..
def get_min_number():
    n = input()
    sum_of_bracket = 0
    number = ''
    answer = 0
    bracket = True #괄호는 오픈

    # 괄호 안에 있는 더하기 or 그냥 더하기 구분 필요
    # 언제 괄호가 닫히나요?
    # 1. 식이 끝난 경우
    # 2. 다음 - 부호가 있는 경우!

    for element in n:
        if element == '-':
            # 괄호를 닫고, 기존 모든 값들을 더해주세요
            if bracket:
                answer += sum_of_bracket + int(number)
            else:
                answer -= sum_of_bracket + int(number)
            #괄호 새로 오픈
            sum_of_bracket = 0
            #음수 괄호 오픈
            bracket = False
            number = ''
        elif element == '+':
            sum_of_bracket += int(number)
            number = ''
        else:
            number += element
    if bracket:
        answer += sum_of_bracket + int(number)
    else:
        answer -= sum_of_bracket + int(number)

    print(answer)
