# 정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.
# 고찰1: python snake case 지향
def get_the_rest(num1, num2):
    return num1 % num2


# 정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.
def same_number(num1, num2):
    if num1 == num2:
        return 1
    return -1


# 머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.
# 나이 구하기 : 나이 = 현재 연도 - 출생 연도 + 1
# 출생 연도 = 현재 연도 + 1 - 나이
def get_age(age):
    current_year = 2022
    return current_year + 1 - age


# 예각 - 1: 0 < angle < 90
# 직각 - 2: angle = 90
# 둔각 - 3: 90 < angle < 180
# 평각 - 4: angle = 180
def get_angle(angle):
    if 0 < angle < 90:
        return 1
    if angle == 90:
        return 2
    if 90 < angle < 180:
        return 3
    return 4


# 머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다.
# 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다.
# 정수 n과 k가 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.
# 음료수의 개수 = 주문한 음료 + n/10
def get_price(n, k):
    return n * 12000 + (k - n // 10) * 2000


# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
# 가우스 공식: 모두 더한 값
def get_even_sum(n):
    std = n // 2
    return std * (std + 1)


# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
# 1안 : numpy의 평균 함수 이용 > 속도가 매우 느림 but, 다차원 배열의 합도 한 번에 가능
# 2안 : python 기본 함수 sum() 이용
# import numpy

def get_array_mean(numbers):
    return sum(numbers) / len(numbers)
    # return numpy.mean(numbers)


# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
# 1안 : 루프를 한 번 돈다, O(n)
# 1안 B : python 기본 함수 count() > 배열 , 문자열

def count_num(numbers, n):
    return numbers.count(n)


# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.

def get_pizza_num(n):
    if n % 7 == 0:
        return n // 7
    return n // 7 + 1
    # return (n - 1) // 7 + 1


# n - 1 의 경우, n > 0 이므로 피자는 반드시 한 판 이상이고, 7의 배수에 예외 처리하지 않아도 됨


# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
# 1안 : 반복문을 이용해서 개수를 구한다.

def divide_num(num_list):
    # odd = sum(1 for n in num_list if n % 2)
    even_count = 0
    for num in num_list:
        if num % 2 == 0:
            even_count += 1
    odd_count = len(num_list) - even_count
    return [even_count, odd_count]


# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

def get_2X_array(numbers):
    return [i * 2 for i in numbers]


# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

# "".join(reversed(my_string))
# reversed
# 테스트 1 〉	통과 (0.00ms, 9.97MB)
# 테스트 2 〉	통과 (0.00ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 9.96MB)
# 테스트 4 〉	통과 (0.00ms, 10.1MB)
# 테스트 5 〉	통과 (0.00ms, 9.99MB)

# my_string[::-1]
# 테스트 1 〉	통과 (0.00ms, 10MB)
# 테스트 2 〉	통과 (0.00ms, 10.1MB)
# 테스트 3 〉	통과 (0.00ms, 10.1MB)
# 테스트 4 〉	통과 (0.00ms, 10MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)

def get_reverse_string(my_string):
    # return "".join(reversed(my_string))
    return my_string[::-1]
