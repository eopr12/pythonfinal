# 왜 반복을 사용하나?


# 순차문
print("# 순차문 시작")
print("환영합니다")
print("환영합니다")
print("환영합니다")
print("환영합니다")
print("환영합니다")
print("# 순차문 종료")


# for 문을 이용하여 "환영합니다"를 다섯번 출력하시오
print("# for 문 시작")
for x in range(0, 5, 1):
    print("환영합니다")
print("# for 문 종료")

# while 문을이용하여 "환영합니다"를 다섯번 출력하시오
print("# while 문 시작")
i = 0
while i<5:
    print("환영합니다")
    i = i + 1 # 조건식을 처리하기 위한 문장.
print("# while 문 종료")