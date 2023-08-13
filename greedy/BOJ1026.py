import sys

# 배열 개수 입력 받기
n = int(input())
# A 배열 입력 받기
# list_A = list(map(int, input().split()))
list_A = list(map(int, sys.stdin.readline().rstrip().split()))
# B 배열 입력 받기
list_B = list(map(int, sys.stdin.readline().rstrip().split()))

# list_A 오름차순 정렬
list_A.sort()
# list_B 내림차순 정렬
list_B.sort(reverse=True)

# 두 리스트 곱
# result = map(lambda a, b: a * b, list_A, list_B)
# print(sum(result))

sum = 0
for i in range(n):
    sum += list_A[i]*list_B[i]

print(sum)
