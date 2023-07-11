def get_3x_num(n):
    i = idx = 0
    while True:
        i += 1
        if i % 3 == 0 or str(i).count('3') > 0:
            continue
        idx += 1
        if n == idx:
            return i
    return 0

import re

def get_polynomial(polynomial):
    x = 0
    constant = 0
    for mono in re.split('[ +]',polynomial):
        if 'x' in mono:
            print("x")
            x += int(mono.split('x')[0])
    print(x+" "+constant)