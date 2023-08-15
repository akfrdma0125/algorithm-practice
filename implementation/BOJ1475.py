import collections

text = input()
# ex_counter = collections.Counter(text)
# numOf9 = ex_counter['9']
# ex_counter['9'] = 0
# ex_counter['6'] += numOf9
# if ex_counter['6'] % 2 == 1:
#     ex_counter['6'] += 1
# ex_counter['6'] = ex_counter['6']//2
# print(max(ex_counter.values()))

arr = [0 for i in range(10)]

for i in text:
    arr[ord(i) - ord('0')] += 1

arr[6] += arr[9]
arr[9] = 0
if arr[6] % 2 == 1:
    arr[6] += 1
arr[6] = arr[6]//2



print(max(arr))