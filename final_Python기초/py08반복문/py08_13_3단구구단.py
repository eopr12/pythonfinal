
# while 문을 사용하여 3단을 출력하시오.
i = 1
while i<= 9:
    str = "i=%s , %s * %s = %2s" % ( i, 3, i, 3*i )
    print( str )
    i = i + 1 # i를 1씩 증가시키면서 

print( "while 문 종료")