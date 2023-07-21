# 지수 표현 방식 기본적으로 실수형태로 들어감
import sys

a = 1e9  # 1*10의 9승

# 실수형은 정보를 표현하는 정확도에 한계를 가짐, 이진수 체계라서
0.3 + 0.9 != 0.9

# solution round() method
round(0.3 + 0.6, ndigits) == 0.9

# 리스트 자료형
# c의 배열과 연결 리스트와 유사한 기능
# [] 와 쉼표로 원소 구분 / 인덱스로 접근
a = [1, 2, 3, 4]
b = [0] * 10  # 0이 10번 들어간 리스트

# 인덱싱: 인덱스 값으로 접근하는 방법
# 음수: 뒤에서부터 n번째 원소
# 슬라이싱: 파이썬의 유용한 부분 [a:b] a~b-1까지..

print(a[1:4])  # 1,2,3

# 리스트 컴프리헨션
# 반복문뿐만 아니라 조건문도 사용 가능
# 반복문 먼저 넣어서 작성하는 것을 추천
arr = [i for i in range(10)]  # 0,1,,,9
array = [i for i in range(10) if i % 2 == 1]  # 홀수인 수만 원소에 담을 것

# 2차원 리스트를 초기화할 때 효과적으로 사용
n,m = 4,3
arr2by2 = [[0]*m for _ in range(n)] # n*m 의 이차원 배열

# 반복문 안에 언더바 _ 는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때

# 파이썬 리스트에서 특정 값을 가지는 원소를 모두 제거하기
# 왜냐면, 파이썬은 특정 값을 가지는  원소 하나만 제거하므로: remove()
remove_set = {3,5} #집합 자료형

result_arr = [i for i in arr if not in remove_set] #remove_set 에 포함되지 않는 값들만 저장
print(result)

# 문자열 자료형
# 큰따옴표로 구성하는 경우 내부적으로 작은따옴표 사용 가능/ 역도 가능
# 문자열도 리스트와 비슷하게 사용 가능하나, 변경은 불가능 (immutable)

# 튜플 자료형
# 리스트와 유사하나, 한 번 선언된 값을 변경할 수 없음
# 소괄호 이용, 리스트에 비해 공간 효율적

# 알고리즘에서 활용
# 서로 다른 성질의 데이터를 묶어서 관리해야 할 때 ex. 최단 경로 알고리즘(비용, 노드번호)
# 데이터의 나열을 해싱의 키 값으로 사용해야 할 때 (변경 불가하므로)
# 메모리를 효율적으로 사용해야 할 때
tuple_1 = (1,2,3,4,5)

# 사전 자료형
# 키와 값의 쌍을 데이터로 가지며 키는 임의의 변경 불가능한 자료형을 이용, 순서X, indexX
# 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1) 의 시간이 소요됨
dic = dict()
dic['key'] = 'value'

if 'key' in dic:
    print("exist")

# 집합 자료형: 중복과 순서가 없음
# 중괄호에 콤마를 기준으로 원소 구분
# 데이터의 조회 및 수정에 있어서 O(1) 의 시간이 소요됨
# 원소 한 개: add 여러개: update

# 집합이나 사전 자료형의 경우 인덱싱으로 값을 얻을 수 없다는 점

# 입출력
input() # 한 줄의 문자열을 입력받는 문자
map() #리스트의 모든 원소에 대해 각각의 함수를 적용하는 함수
map(int, input().split()) # split한 리스트의 각 원소에 대해 int 함수 적용

# 빠르게 입력 받기
# 이진탐색, 정렬, .. 등 많이 사용
sys.stdin.readline().rstrip()
# rstrip() : 입력 후 엔터 또한 줄 바꿈 기호로 입력되므로 메서드를 함께 사용

# 표준 출력
print() # end = default = \n 이므로 end = " " 등올 변경

# f-string
print(f"정답은 {dic} 입니다.")

# 파이썬의 기타 연산자 in
# 리스트 튜플 문자열 딕셔너리 모두 사용

# pass: 아무것도 처리하고 싶지 않을 때, 조건문 밑에 그냥 'pass'
# 파이썬은 조건문 밑에 구문이 없으면 오류

# 반복문
# 코딩테스트에서는 간결하게 for문을 사용하는 경우가 많음

for var in list:
    pass #source code

# 함수 : 반복되는 작업을 하나의 단위로 묶어 놓아서 코드의 반복을 줄임
# 전역변수 : global name << 선언 필요, 함수에서 사용하고 싶다면!!
# 전역변수를 단순히 사용하는 거라면 (읽기) 그냥 사용 가능
# 그런데 코딩 테스트에서는 리스트는 전역변수로 선언 > 함수에서 활용하는 경우가 많음
# 여러 개의 반환값을 가질 수 있음

# 람다 표현식: 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징이다.
# 한 번 사용하고 말 경우
print((lambda a, b: a+b)(3,7))
# a,b를 매개변수로 받아서 ':' 뒤에 있는 내용을 수행함
# 3+7 = 10 , 10을 출력

# 시례: sort와 같이 한 번 사용할 경우, sorted 에서 빈번히 사용
ex_arr= [('a',1),('b',2),('c',3)]
# 두번째 원소를 기준으로 정렬하고 싶을 때

def my_key(x): return x[1]

print(sorted(ex_arr, key= my_key)) # key는 매개변수가 함수인 함수
print(sorted(ex_arr, key= lambda x:x[1])) # lambda식으로 my_key와 동일한 내용 선언

print(map(lambda a,b: a+b, list1, list2)) # 리스트의 같은 인덱스끼리 더함

# 라이브러리
# itertools(순열, 조합: 완전 탐색), heapq(다익스트라), bisect(이진탐색),collections, math

print(eval("3-78")) # 자연어 수식을 계산하는 함수
# 순열과 조합
# Counter 등장 횟수를 세는 기능,각각의 원소가 몇 번씩 등장했는지..

# math
# gcd : 최대 공약수
