# 정수 2개를 입력 받고 반복문를 이용하여 "시작값"부터 "종료값"까지 의 합계를 구하시오. 
# 프로그램을 최대한 작은 조각으로 분리하여 작성한다.
# 
# 실행결과예시
#   시작값을 입력하세요.  1
#   종료값을 입력하세요.  4
#   1부터 4까지의 합계는 10입니다
# 
#   시작값을 입력하세요.  4
#   종료값을 입력하세요.  1
#   1부터 4까지의 합계는 10입니다

# main 함수의 처리 순서
#   1. 데이터 수집 
#   2. 데이터 처리
#       2.1 리스트 정렬
#   3. 합계 구하기 ==> 합계 구하는 함수 만들기
#       
#       여기 2. 에서 반환되는 리스트는 아래와 같다
#           0번방 값은 시작값 ==> 예시: 1
#           1번방 값은 종료값 ==> 예시: 4
#           2번방 값은 합계값 ==> 예시: 10
#   4. 데이터 출력

# 데이터 수집
# readList 반환값은 리스트라고 가정
def newmethod309():
    result = None
    첫번째정수 = input( "정수를 입력하시오")
    result = int( 첫번째정수 )
    return result 

def readList():
    result = None    
    result = []
    반환값 = newmethod309()
    result.append(반환값 ) # result[0] = 1

    반환값 = newmethod309()
    result.append(반환값 ) # result[1] = 4

    return result # 리스트를 반환


# 데이터 처리 : 오름차순으로 리스트 정렬
# nlist : 리스트다.
def processList(nlist):
    result = None
    result = sorted( nlist )
    return result # 0번방값: 1, 1번방값: 4

# 데이터 합계 : 
# 매개변수 nlist: 리스트다
def sumList( nlist ):
    result = 0 # 합계를 구하기 위해서 None 대신 0 으로 초기화 
    for i in nlist:
        result = result  + i # i의 의미: i 번째 방의 값을 의미한다.
    return result # 합계값


# 데이터 출력
# 매개변수 nlist: 리스트다
def printList(nlist):
    result = None
    result = "%s부터 %s까지의 합계는 %s입니다" % ( nlist[0], nlist[1], nlist[2] )
    print( result )
    return result # 

# 프로그램 시작
def main():
    result = None

    # main 함수의 처리 순서
    # 1. 데이터 수집 ==> readList() 함수 사용
    # 2. 데이터 처리 ==> processList() 함수 사용
    # 3. 데이터 합계 ==> sumList() 함수 사용
    # 4. 데이터 출력 ==> printList() 함수 사용
    result = readList() # 리스트가 반환됨. result 는 리스트다. 
    result = processList( result ) # result == [시작값, 종료값] 
    
    # 합계값을 구하고 result 리스트에 추가. 
    합계값 = sumList( result ) # 
    result.append( 합계값 ) # result == [시작값, 종료값, 합계값]

    result = printList( result ) # <-- 여기서의 result는 문자열이다.

    return result

# 이 모듈이 단독으로 사용되면 main()를 호출하라.
main()
