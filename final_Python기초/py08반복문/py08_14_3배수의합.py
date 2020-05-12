# while 문을 사용하여 1부터 100사이의 3의 배수의 합을 계산하여 출력하는 프로그램을 작성하시오.
# ※ 3의 배수는 나머지 연산자를 이용하여 구한다. 3의 배수이면 sum 하고 아니면 pass
#
# 
# 1부터 100 사이의 3의 배수의 합은 1683입니다.


sum = 0
for i in range(1, 101 , 1) :
    # 3의 배수이면 sum을 아니면 pass
    # 3의 배수 <==> i%3 == 0
    if i%3 == 0:
        sum = sum + i
    else:
        pass
print( sum )

i = 1
sum = 0
while i<=100 :
    # 3의 배수이면 sum을 아니면 pass
    # 3의 배수 <==> i%3 == 0
    if i%3 == 0:
        sum = sum + i
    else:
        pass

    # i를 1씩 증가시키면서 
    i = i + 1

str = "%s 부터 %s 사이의 3의 배수의 합은 %s 입니다." % ( 1, 100, sum )
print( str )