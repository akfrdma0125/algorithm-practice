def calculate_nums(s):
    arr = s.split(' ')
    back = 0
    answer = 0
    for element in arr:
        if element == 'Z':
            answer -= back
            continue
        back = element
        answer += element
    return answer
