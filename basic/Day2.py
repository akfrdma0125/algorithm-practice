# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
# 1안. 루프를 돌면서 해당 문자가 있으면 문자열을 추가하지 않음
# 2안. replace > 파이썬 사용자들이 주로 사용하는 방법!!

def delete_letter(my_string, letter):
    return my_string.replace(letter, '')


# 두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.
# 1안. 루프를 돌면서 확인하는 경우

# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (0.00ms, 10MB)
# 테스트 3 〉	통과 (0.00ms, 10.2MB)
# 테스트 4 〉	통과 (0.00ms, 10MB)
# 테스트 5 〉	통과 (0.00ms, 10.1MB)
# 테스트 6 〉	통과 (0.00ms, 10.1MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)
# 테스트 8 〉	통과 (0.00ms, 10.1MB)

def get_similarity(s1, s2):
    count = 0
    for s1_element in s1:
        if s1_element in s2:
            count += 1
    return count


# 2안. 집합 자료형 이용 (집합은 중복이 불가능하므로!!)

# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)

def get_similarity_by_set(s1, s2):
    return len(set(s1) & set(s2))


# rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.
# 가위 2 > 주먹 0
# 주먹 0 > 보 5
# 보 5 > 가위 2

def win_rock_scissor_paper(rsp):
    result = []
    for i in range(len(rsp)):
        if rsp[i] == '2':
            result.append('0')
        elif rsp[i] == '0':
            result.append('5')
        else:
            result.append('2')
    return ''.join(result)


# 자료형 dictionary 이용
def win_rock_scissor_paper_dictionary(rsp):
    d = {'0': '5', '2': '0', '5': '2'}
    return ''.join(d[i] for i in rsp)


# 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.
def rotate_array(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]


# 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.
# a는 0, b는 1, c는 2, ..., j는 9입니다.
# 아이디어 (남의) : chr(int(i)+97) char <-> int 의 관계 !!
def get_programmer_age(age):
    age_str = str(age)
    d = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'}
    return ''.join(d[i] for i in age_str)


# 머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.
# 개수 >> count 를 생각해보기 !!
def get_claps(order):
    # claps = ['3', '6', '9']
    # count = 0
    # for element in str(order):
    #     if element in claps:
    # or 이 부분을 >> if element%3 == 0 << 로 해도 메모리 낭비가 적고 좋을 듯 ..
    #         count += 1
    # return count
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')


# 문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
# 집합은 순서가 보장이 되지 않으므로, 기각
def delete_duplication(my_string):
    result = []
    for i in range(len(my_string)):
        if my_string[i] in result:
            continue
        result.append(my_string[i])
    return ''.join(result)


# return ''.join(dict.fromkeys(my_string))

# 문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.
# 같은 글자를 만들 수 있는가? > 원소의 개수가 같으면 만들 수 있다!

def make_same_word(before, after):
    before_set = set(before)
    after_set = set(after)
    # 1. 원소가 같은지 확인
    if after_set != before_set:
        return 0
    # 2. 원소의 개수 확인
    for element in after_set:
        if before.count(element) != after.count(element):
            return 0
    return 1


# 순서와 상관 없는데 개수는 상관 있는 경우: sort!!
def make_same_word_sort(before, after):
    return 1 if sorted(before) == sorted(after) else 0
