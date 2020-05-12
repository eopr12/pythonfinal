# 변수의 유효 범위(Scope)


def foo():
    a = 3
    b = 5

    def bar():
        b = 7
        c = 11

        a = b + c
        print(a, b, c) # 18 7 11

    print(a, b)  # 3, 5
    bar()
    print(a, b)  # 3, 5

foo()
