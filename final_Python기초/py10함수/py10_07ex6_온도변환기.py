# 사용자 함수 만들기
# 섭씨 온도를 화씨 온도로, 또 그 반대로 변환하는 프로그램을 작성하여 보자.
# 
#  'c' 섭씨온도에서 화씨온도로 변환
#  'f' 화씨온도에서 섭씨온도로 변환
#  'q' 종료
# 메뉴에서 선택하세요.c
# 섭씨온도: 100
# 화씨온도: 212.0
#  'c' 섭씨온도에서 화씨온도로 변환
#  'f' 화씨온도에서 섭씨온도로 변환
#  'q' 종료
# 메뉴에서 선택하세요.


def printOptions():
    print(" 'c' 섭씨온도에서 화씨온도로 변환")
    print(" 'f' 화씨온도에서 섭씨온도로 변환")
    print(" 'q' 종료")


def C2F(c_temp):
    return 9.0 / 5.0 * c_temp + 32


def F2C(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0


printOptions()
choice = input("메뉴에서 선택하세요.")
while choice != "q":
    if choice == "c":
        temp = float(input("섭씨온도: "))
        print("화씨온도:", C2F(temp))
    elif choice == "f":
        temp = float(input("화씨온도: "))
        print("섭씨온도:", F2C(temp))
    printOptions()
    choice = input("메뉴에서 선택하세요.")
