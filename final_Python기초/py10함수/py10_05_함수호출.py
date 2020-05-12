# 함수 호출 과정을 이해한다.
# 매개변수들
# 함수를 호출할 때 함수에서 사용할 데이터가 전달된다.
# 인자(argument) a,b 는 순서대로 매개변수(parameter) x, y 에 대입된다.
# x = a
# y = b


def add(x,  y):  # x, y 는 매개변수라고 칭한다.
    result = x + y
    return result


a = 3
b = 4
value = add(a, b)  # a,b 는 인자라고 칭한다
print(value)
