# 숫자 입력 받기
x = input( "정수 입력")
y = input( "정수 입력")
z = input( "정수 입력")

# 문자열 정수 변환
x = int( x )
y = int( y )
z = int( z )

# x, y, z 를 비교
if x > y:    
    # 여기서 비교해야 값들을 무엇인가?
    # x와 z를 비교해야 한다.
    if x > z:
        print("입력받은 수 중 가장 큰수는 ", x, "입니다")
    else:
        print("입력받은 수 중 가장 큰수는 ", z, "입니다")
else:
    # 여기서 비교해야 값들을 무엇인가?
    # y와 z를 비교해야 한다.
    if y > z:
        print("입력받은 수 중 가장 큰수는 ", y, "입니다")
    else:
        print("입력받은 수 중 가장 큰수는 ", z, "입니다")

# if ~ elif ~ else 로 바꾸어 보기
if x > y and x > z:
    print("입력받은 수 중 가장 큰수는 ", x, "입니다")
elif y > z:
    print("입력받은 수 중 가장 큰수는 ", y, "입니다")
else:
    print("입력받은 수 중 가장 큰수는 ", z, "입니다")


# max 함수를 사용하여 최대값 구하기
maxvalue = max( x, y, z )
print("입력받은 수 중 가장 큰수는 ", maxvalue, "입니다")
