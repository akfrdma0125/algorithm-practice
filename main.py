# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import day1.Day1

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    temp = 'soooooooom'
    temp_list = list(temp)
    temp_list.reverse()
    print(''.join(temp_list))
    reverse_temp = "".join(reversed(temp))
    reverse_v2 = temp[::-1]
    print(reverse_v2)