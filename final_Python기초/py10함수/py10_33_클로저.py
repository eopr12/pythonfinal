# 변수의 유효 범위(Scope)


def outer_func(tag):  # 1
    text = "Some text"  # 5
    tag = tag  # 6

    def inner_func():  # 7
        str = "<%s> %s </%s>" % (tag, text, tag)  # 9
        return str

    return inner_func  # 8


h1_func = outer_func("h1")  # 2
p_func = outer_func("p")  # 3

print(h1_func())  # 4
print(p_func())  # 10
