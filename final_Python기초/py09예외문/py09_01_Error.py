
# 숫자가 아닌 것을 정수로 변환하려고 할 때
# 숫자가 아닌 것을 실수로 변환 할 때
# 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환하려고 할 때

# 테스트 방법
# 테스트1. abc 입력
# 테스트2. 숫자 0 입력
# 테스트3. 숫자 12.5 입력
# 테스트4. 숫자 12 입력

# 오류의 종류에 따라서 서로 다른 예외 처리가 가능하다

try:    
    입력값 = input("숫자를 입력하세요")
    정수값 = int( 입력값 ) # 입력값 "abc" 이면 에러 발생
    실수값 = float( 입력값 ) # 입력값 "abc" 이면 에러 발생
    실수값 = int( 입력값 ) # 입력값 "12.5" 이면 에러 발생
    나누기 = 10 / 정수값 # 정수값 0이면 오류 발생.
except ZeroDivisionError as ex:
    print("ZeroDivisionError ::", ex )
    pass
except TypeError as ex:
    print("TypeError ::", ex )
    pass
except ValueError as ex: # 무조건 마지막에 넣어야 한다.
    print( "ValueError ::",  ex )
    pass
except Exception as ex: # 무조건 마지막에 넣어야 한다.
    print( "Exception ::",  ex )
    pass
print("정상 종료")