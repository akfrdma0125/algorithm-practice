def get_near_number(n, array):
    array.sort()

    dif_min = abs(array[0] - n)
    idx = 0

    for i in range(1, len(array)):
        dif = abs(array[i] - n)
        if dif < dif_min:
            idx = i
            dif_min = dif

    return array[idx]


# python 문자열 정렬
# sorted(str) > 문자열 정렬이 되지 않는다!
# 그런데 .. ''.join(sorted(result))는 된다?

def get_char_once(s):
    set_s = set(s)
    result = ""
    for element in set_s:
        if s.count(element) == 1:
            result += element
            print(element)
    return ''.join(sorted(result))
    # sorted(result)
    # return result


# 슬라이싱은 범위를 초과 해도 에러가 나지 않음!
def get_str_array(my_str, n):
    result = []
    offset = 0
    while offset < len(my_str):
        result.append(my_str[offset:offset + n])
        offset += n
    return result


def get_diagnosis_order(emergency):
    temp = sorted(emergency, reverse=True)
    result = []
    for element in emergency:
        result.append(temp.index(element) + 1)
    return result


# dict
def get_diagnosis_order_dict(emergency):
    answer = []
    emer_ls = {e: i + 1 for i, e in enumerate(sorted(emergency)[::-1])}
    for e in emergency:
        answer.append(emer_ls[e])
    return answer


def translate_number(my_str):
    num_dict = {
        'zero': '0',
        'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6',
        'seven': '7', 'eight': '8', 'nine': '9'}
    for num in num_dict:
        my_str = my_str.replace(num, num_dict[num])
    return my_str


def check_spell_set(spell, dic):
    spell_set = set(spell)

    for element in dic:
        # 조건 '모두'
        if len(spell_set - set(element)) != 0:
            continue

        counts = [element.count(i) for i in spell_set]

        if counts.count(1) == len(spell_set):
            return 2

    return 1

def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2
