# 원의 넓이와 둘레를 동시에 반환하는 함수를 작성하여 본다.
# 예시)
# 원의 반지름을 입력하시오: 10
# 원의 넓이는 314.1592653589793이고 
# 원의 둘레는 62.83185307179586이다.

# pi=3.141592... 를 사용하기 위해서 math 모듈 임포트
import math 

def circle( radius) :
    넓이 = math.pi * radius * radius
    둘레 = 2 * math.pi * radius
    return ( 넓이, 둘레 ) # 튜플 자료구조 1개를 리턴하는 것이다

# main 함수 정의 
def main():
    str = input( "원의 반지름을 입력하시오")
    radius = float( str ) # 문자열을 실수로 변환.
    # 원의 넓이와 둘레를 계산한다
    (x, y) = circle( radius ) # x==넓이, y==둘레 

    tmp = "원의 넓이는 %10.4f ,  둘레는 %10.4f 이다 " % ( x, y )
    print( tmp )

# main 함수 호출
if __name__ == "__main__":
    main()

