# 사용자 함수 만들기
# 두 개의 정수가 주어지면 두수 중에서 더 큰 수를 찾아서 이것을 반환하는 함수를 만들어보자. 

# 함수 정의
# 함수이름 : get_max()
# 매개변수 : x  ==> 숫자: 1
# 매개변수 : y  ==> 문자: "2"
# result 는 get_max 함수의 지역변수다.
def get_max(x, y):
    result = None

    try:
        if( x > y ) :
            result = x
        else :
            result = y
    except Exception as ex:
        pass

    return result

def myinput( mesg ) :
    try:
        n1 = input( mesg )
        n1 = int( n1 )
    except ValueError as ex:
        print( ex )

    return n1
	
	
# main 함수를 만들고 사용한다.
# 왜 main() 함수를 만들어 사용하는가?
# 프로그래밍에서 지향하는 방식은 전역변수를 사용하지 않는다. 
# 첫번째정수, 두번째정수, value 는 main 함수의 지역변수다.
def main() :
    try:
        첫번째정수 = myinput( "첫번째 정수 입력: " )
        두번째정수 =  myinput( "두번째 정수 입력: " )

	    value = get_max(첫번째정수, 두번째정수)
	    print(value)
    
	    value = get_max(10, "20") # value값은 무엇일까요? ==> None
	    if( value == None ) :
	        print("error이므로 다시 입력하세요")
	    else :
	        print(value)
    except Exception as ex:
        pass

# main 함수 호출. main() 함수가 프로그램의 시작점이 된다. 
main() #