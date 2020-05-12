# 변수의 유효 범위(Scope)

x = 1
print(x)  # ???

def outer():
    y = 5
    print(x)  # ???
    print(y)  # ???

outer()
