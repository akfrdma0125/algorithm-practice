# This is a sample Python script.
import re
from typing import Union, Any

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Implementaion
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def solve(tables):
    tables.sort(key=lambda x: x[0])
    tables.sort(key=lambda x: x[1])
    before_end = tables[0][1]
    count = 1
    for (begin, end) in tables[1:]:
        if begin >= before_end:
            count += 1
            before_end = end
    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_time = time.time()

    Implementaion.play_game()
    # program 소스코드

    end_time = time.time()
    print("time :", end_time - start_time)
