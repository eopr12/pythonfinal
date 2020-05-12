# 변수의 유효 범위(Scope)

x = 1
print(x)

if(True):
    y = 5
print(y)  # ??


for z in range(1, 5, 1):
    pass
print(z)  # ??


def outer():

    if(True):
        y = 5

    print(y)  # ??


outer()
