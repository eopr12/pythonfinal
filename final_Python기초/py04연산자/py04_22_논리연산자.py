# py04_22_논리연산자.py
# 변수 선언과 초기화
x = 3
y = 4

print("x : ", x)
print("y : ", y)

r = ((x == 3) and (y == 3))  # True and False
print("( x == 3 ) && ( y == 3 ) : ", r)

r = ((x == 3) and (y != 3))  # True and True
print("( x == 3 ) && ( y != 3 ) : ", r)

r = ((x == 3) or (y == 3))  # True or False
print("( x == 3 ) || ( y == 3 )  : ", r)

r = ((x == 3) or (y == 4))  # True or True
print("( x == 3 ) || ( y == 4 ) : ", r)

r = ((x != 3) or (y == 4))  # False or True
print("( x != 3 ) || ( y == 4 ) : ", r)

r = ((x != 3) or (y != 4))  # False or False
print("( x != 3 ) || ( y != 4 ) : ", r)

print((x == y) and (x != y))

print((x > y) or (x < y))

print((x >= y) or (x <= y))

print((x == y) and (x != y) or (x < y))
