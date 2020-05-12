# 사용자 함수 만들기
# 정수를 입력받아서 제곱한 값을 반환하는 square() 함수를 만들어보자.


# 함수 정의
# 함수이름 : square
# 매개변수 : n
def square( n , 승수) :
    result = None 
    # 반환값을 왜 None으로 초기화 하는가? 
    # 함수에서 retrun 문이 없으면 None 반환.
    # 함수에서 retrun 문이 있으면 값이 반환.
    
    # 가정 n 문자열이면 에러발생. 어떻게 처리할까?
    try:
        result = n ** 승수
    except Exception as ex:
        pass # 로그에 출력하도록 변경. 
     
    return result
    
# 함수 호출
value = square( 10 , 2) # ==> 100
print( value ) # ==> 100
value = square( 10 , 10) # ==> 1000000000000
print( value ) # ==> 10000000000
