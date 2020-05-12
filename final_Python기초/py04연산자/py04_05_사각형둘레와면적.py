# py04_05_사각형둘레와면적.py

w = input("너비 값을 입력하시오 >> ") # 문자열
h = input("높이 값을 입력하시오 >> ") # 문자열

try:
    w = float( w ) # 실수로 형변환 
    h = float( h ) # 실수로 형변환 
except ValueError:
    pass

area = w  * h
perimeter = 2 * (w + h)

print( "사각형의 넓이:", area)
print( "사각형의 둘레:", perimeter)
