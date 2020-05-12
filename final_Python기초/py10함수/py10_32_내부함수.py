# 변수의 유효 범위(Scope)
# 내부 함수


def parent():
    a = 100
    b = 200

    # child() 내부 함수 정의

    def child():
        b = 300

        print(a)
        print(b)

    child()


parent()
