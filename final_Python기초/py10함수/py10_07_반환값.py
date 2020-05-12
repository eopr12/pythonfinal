# 함수 반환값


def getSum(start, end):
    sum = 0
    for i in range(start, end, 1):
        sum = sum + i

    return sum


value = getSum(1, 10)
print( value ) # 55


def getMax(a, b):
    result = 0
    if a > b:
        result = a
    else:
        result = b
    return result

value = getMax(1, 10)
print( value ) # 10