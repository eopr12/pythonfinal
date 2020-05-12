
# 매개변수로 불린,숫자,문자열 자료형을 받으면 원본은 바뀌지 않는다
# 원복값 복사 
# 왜 안 바뀌는가?
# 어떻게 하면 될까?

def swap(a, b):
    # a-->b, b-->a
    temp = b
    b = a
    a = temp
    print('swap 안: a=', a, ', b=', b)


def main():
    # 변수의 선언과 초기화
    a = 5
    b = 3

    print('swap 전: a=', a, ', b=', b)
    swap(a, b)
    print('swap 후: a=', a, ', b=', b)

main()