import time

start_time = time.time()

# program 소스코드

end_time = time.time()
print("time :", end_time - start_time)  # 수행시간 출력



# input

# default 입력 받은 리소스는 기본 자료형 : str
input()
# 자료형 변경
자료형(input())
# 여러 개의 자료형 반환
input().split() # 리스트 반환 , 근데 자료형이 str인 ..
A,B = input().split() # 공백을 기준으로 첫 번째 원소 : A, 두 번째 원소 : B

# 그러면 정수로 바꾸고 싶으면 ..?
A, B = int(input()).split() # 오류: string 을 int로 바꿀 수 없는 경우 :'11 22'
A, B = int(input().split()) # 오류: list를 int 로 바꿀 수 없음!!

# map 함수
A,B = map(자료형, 리스트)
# 실례
A,B = map(int, input().split())






