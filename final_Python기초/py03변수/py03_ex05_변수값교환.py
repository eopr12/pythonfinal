# 변수 x 와 변수 y의 값을 서로 바꾸는 프로그램을 작성해보자.
# 다음과 같은 프로그램으로는 변수의 값을 교환할 수 없다. 
# 왜 그럴까? 그리고 해결 방법은 무엇일까? 외팔이 기법을 사용

x = 10
y = 20

print( "x, y =", x, ",", y )

temp = x
x = y
y = temp 
print( "x, y =", x, ",", y )

