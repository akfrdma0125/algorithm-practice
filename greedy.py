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

