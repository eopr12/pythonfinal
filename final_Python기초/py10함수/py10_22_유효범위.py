# 변수의 유효 범위(Scope)


x = 1
print(x)


def outer():

    if(True):
        y = 5

    print(y)  # ??


outer()
print(y)
