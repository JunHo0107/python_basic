# 반복문

# 콘솔창에 Hello 를 10번 출력

# 반복문을 이용해서 Hello 10번 출력
for i in range(0, 10):
    print("Hello")

# range(0,10) 는 배열 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 와 같다고 생각
print(range(0, 10))
print(list(range(0, 10)))

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("Hello")

# 콘솔창에 1부터 10까지 출력
# 반복문을 이용하는 가장 큰 이유 >> 중복코드 합치기
for i in range(1, 11):
    print(i)

numArray = [2, 5, 3, 4]
for i in numArray: # 일반 배열도 in 옆에 사용가능
    print(i)

stuArray =["김호빵", "이찐빵", "박꿀빵"]
for i in stuArray:
    print(i)

# numArray 모든 값에 3을 곱하기
numArray = [2, 5, 3, 4]
print(numArray * 3) # [2, 5, 3, 4, 2, 5, 3, 4, 2, 5, 3, 4], 결과값만 도출 되었을 뿐, numArray 처음 값은 변동 X

# 배열 내 값 수정
print(numArray) # [2, 5, 3, 4]
print(numArray[0]) # 2
print(numArray[0] * 3) # 6

numArray[0] = numArray[0] * 3
print(numArray[0]) # 6

numArray[1] = numArray[1] * 3
print(numArray)

numArray[2] *= 3
print(numArray)
numArray[3] *= 3
print(numArray)

print(numArray * 3)
# for 문으로 바꿔보기.
numArray[0] *= 3
numArray[1] *= 3
numArray[2] *= 3
numArray[3] *= 3
print(numArray)

numArray = [2, 5, 3, 4]
print(numArray)

# i가 0, 1, 2, 3이 되도록 하는 for문
for i in range(0, len(numArray)): # 0 ~
    numArray[i] *= 3

print(numArray)

# 다른 사람이 만든 배열 라이브러리 numpy 라이브러리 사용
# numpy 라이브러리 불러오기
import numpy as np  # as는 alias(별칭)의 약자

numArray = [2, 5, 3, 4]
npArray= np.array([2, 5, 3, 4])

print(numArray)
print(npArray)

print(type(numArray)) # <class 'list'>
print(type(npArray)) # <class 'numpy.ndarray'>

print(npArray * 3)
print(npArray)

npArray = npArray * 3
print(npArray)

npArray *= 3
print(npArray)

#  1부터 100까지 다 더하면 ?
#  i 가 1부터 100이 되도록 for문 만들기

sum = 0
for i in range(1, 101):
    sum += i

print(sum)  #5050

#  5팩토리얼 값은? 5! -> 5 * 4 * 3 * 2 * 1 = 120
sum = 1
for i in range(1, 6):
    sum *= i
print(sum)

# 10! -> 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800
sum = 1
for i in range(1, 11):
    sum *= i

print(sum)

# range로 거꾸로 배열 생성
for i in range(10, 0, -1):
    print(i)

# 1부터 30까지 숫자 중에 홀수만 출력
# i가 1부터 30이 되도록 for문 생성
for i in range(1, 31):
    # i가 1~30이 되는데, i가 홀수인지 체크 (조건 체크)
    if i % 2 == 1:
        print(i)

# 30부터 60까지 중에 짝수만 다 더하면 ?
# i가 30부터 60이 되도록 for문 생성
sum = 0
for i in range(30, 61):
    # i가 짝수인지 확인
    if i % 2 == 0:
        # 값을 더하기
        sum += i

print(sum) # 위 124-128 까지의 for문 종료 후 실행

# range의 범위 조정
sum = 0
for i in range(30, 61, 2): # [30, 32, 34, 36, ..., 60]
    sum += i

print(sum)

nameArray = ["김호빵", "이찐빵", "박꿀빵", "김식빵"]

# 김씨 성을 가진 사람이 몇 명인지 세어 보기
sum = 1
for i in nameArray:
    print(i) # i 는 "김호빵", "이찐빵", "박꿀빵", "김식빵"
    # i의 첫번재 글자만 꺼내기
    fst = i[0]
    print(fst)
    # 꺼낸 첫번째 글자 '김'인지 조건 체크
    if fst == '김':
        # 조건이 True면 sum에 1 더하기
        sum += 1

print(sum)


# 콘솔창에
# *
# **
# **
# ***
# ****
# *****
# 와 같이 출력되도록 반복문 작성

# 빈 문자열(empty)
star = ""

# 5번 반복 for문 선언
print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(0, 5))) # [0, 1, 2, 3, 4]
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(5):
    # for문이 반복될 때마다 star에 "*"를 추가한 후 출력
    star = star + "*"
    print(star)

# 콘솔창에
# *****
# ****
# ***
# **
# *

# 출력해보기

star = "*******"

# 5번 반복하는 for문 생성
print(list(range(5))) # [0, 1, 2, 3, 4]

# for문이 반복될 때마다 star의 길이를 1칸씩 줄인다
# star = star[0:5]
# print(star)
# star = star[0:4]
# star = star[0:3]
# star = star[0:2]
# star = star[0:1]

star = "*******"
for i in range(5, 0, -1): # [5, 4, 3, 2, 1]
    print(star[0:i])

for i in range(5): # [0, 1 ,2 ,3, 4]
    # i 는 0, 1, 2, 3, 4
    # ?는 5, 4, 3, 2, 1
    # 5 - i = ?
    print(star[0:5-i])

# 트리 만들기
#     *
#    ***
#   *****
#  *******
# *********

# print가 5번 실행되므로 5번 반복하는 for문 생성
for i in range(5): # [0, 1, 2, 3, 4]
    # i가 0, 1, 2, 3, 4
    # *는 1, 3, 5, 7, 9 -> i와 관계 : >> 2 * i + 1
    #  는 4, 3, 2, 1, 0 -> i와 관계 : >> 4 - i

    star = ""
    for k in range(2 * i + 1): # 바깥 for 문의 내부 변수 i와 다른 변수명 사용
        star += "*"

    blank = ""
    for k in range(4 - i):
        blank += " "

    print(blank + star)