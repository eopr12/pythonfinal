# 사용자로부터 두 개의 정수를 입력 받아서 둘 중에서 큰 수를 출력하는 프로그램을 작성하여 보자.
# 주의. 문자열로 비교할 때과 숫자로 비교할 때 결과가 다르다.
#
# 변수 2개 만들기 : x,y
#
# 첫번째 키보드에서 입력 받은 값을 x에 넣는다.
# 두번째 키보드에서 입력 받은 값을 y에 넣는다.
#
# x 가 y 보다 크다면 x 값    출력
# 아니면             y 값    출력

x = input("정수를 입력하세요")
y = input("정수를 입력하세요")

x = int(x)
y = int(y)


if x> y:
    print(x, y) 
else:
    print(y, x) 

if x> y:
    print(x, y) 
elif x == y:
    print(x, y)
else:
    print(y, x) 