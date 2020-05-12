# 이 순서도에는 오류가 있다
# 이렇게 예외가 발생하면 어떻게 처리해야 하나?
# 페이지 222~224 참조

s = input("s 입력")

try:
    m = s // 60

    s = s % 60

    print( "m:", m)
    print( "s:", s)
except TypeError as identifier:
    print( identifier )
