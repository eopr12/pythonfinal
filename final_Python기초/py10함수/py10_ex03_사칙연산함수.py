# 두 개의 정수를 입력 받고, 두 수의덧셈, 뺄셈, 곱셈, 나눗셈 
# 결과를 출력하는 프로그램을 작성하시오.

# Add(), Minus(), Mul(), Div() 함수만을 만드시오.  
# 함수 호출을 이용하여 각각의 연산 결과를 출력하시오.
# 입력 받는 것도 함수로 만드시오.
#
# 실행결과예시
# First num : 2
# Second num : 4
# Add : 6    	  ---> Add() 함수를 사용하시오
# Minus : -2	  ---> Minus() 함수를 이용하시오
# Mul : 8         ---> Mul() 함수를 이용하시오
# Div : 0.500000  ---> Div() 함수를 이용하시오

# Add() 함수 정의. 매개변수 2개 사용. x, y 
# Minus() 함수 정의. 매개변수 2개 사용. x, y 
# Mul() 함수 정의. 매개변수 2개 사용. x, y 
# Div() 함수 정의. 매개변수 2개 사용. x, y. ZeroDivisionError 처리 
# myinput() 함수 정의. 정수 입력 처리용 함수. 
# main() 함수 정의.
    # main 함수에서의 작업할 내용.
    # 첫번째 정수 입력 받기
    # 두번째 정수 입력 받기
    # Add() 함수 호출하고 결과값 출력
    # Minus() 함수 호출하고 결과값 출력
    # Mul() 함수 호출하고 결과값 출력    
    # Div() 함수 호출하고 결과값 출력
# main() 함수 호출. main() 함수가 프로그램의 시작점이 된다. 
def Add(  x, y ):
    result = None
    try:
        result = x + y
    except Exception as ex:
        pass    
    return result

def Minus( x, y ):
    result = None
    try:
        result = x - y
    except Exception as ex:
        pass    
    return result
    
def Mul(  x, y ):
    result = None
    try:
        result = x * y
    except Exception as ex:
        pass    
    return result
    
def Div(  x, y ):
    result = None
    try:
        result = x / y
    except ZeroDivisionError as ex:
        pass 
    except Exception as ex:
        pass    
    return result
    
def myinput( ):
    result = None 
    try:
        result = input("입력하세요: ")
        result = int( result )
    except Exception as ex:
        pass    
    return result

# myprint
# 매개변수 2개. str, value
# 함수 호출 사용 예시: myprint( "Add", 10 )
def myprint( str, value ) :
    result = None
    try:
        result = "%s : %s " % (str, value )
    except expression as identifier:
        pass    
    return 

# main() 함수의 역활은 함수들을 조합하는 역활을 담당한다.
# main() 함수의 시작점이 된다.    
def main( ):
    # main 함수에서의 작업할 내용.
    # 첫번째 정수 입력 받기
    # 두번째 정수 입력 받기
    # Add() 함수 호출하고 결과값 출력
    # Minus() 함수 호출하고 결과값 출력
    # Mul() 함수 호출하고 결과값 출력    
    # Div() 함수 호출하고 결과값 출력
    첫번째정수 = myinput() # 첫번째 정수 입력 받기 <==> x
    두번째정수 = myinput() # 두번째 정수 입력 받기 <==> y

    반환값 = Add(첫번째정수 , 두번째정수) # Add() 함수 호출하고 결과를 반환값에 저장
    myprint ( "Add", 반환값) # Add() 함수의 결과값 출력

    반환값 = Minus(첫번째정수 , 두번째정수) # Minus() 함수 호출하고 결과를 반환값에 저장
    myprint ( "Minus", 반환값) # Minus() 함수의 결과값 출력

    반환값 = Mul(첫번째정수 , 두번째정수) # Mul() 함수 호출하고 결과를 반환값에 저장
    myprint ( "Mul", 반환값) # Mul() 함수의 결과값 출력

    반환값 = Div(첫번째정수 , 두번째정수) # Div() 함수 호출하고 결과를 반환값에 저장
    myprint ( "Div", 반환값) # Div() 함수의 결과값 출력

    return 

main( )    
