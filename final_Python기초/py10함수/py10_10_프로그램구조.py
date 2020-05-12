# readList() 함수 : 데이터 수집
# readList 반환값은 리스트라고 가정
# 작업 내용
# 1. 무한 루프 만들고
# 2. 키보드 입력 받고 정수 변환
# 3. 입력 값이 음수이면 루프 탈출 아니면 리스트에 저장한다.
def readList():
    result = None

    result = [] # 리스트 생성
    while True:
        입력값 = input("숫자를 입력하시오: ")
        입력값 = int( 입력값 )

        if 입력값 < 0 :
            break 
        else :
            # 리스트에 추가
            result.append( 입력값 )
    return result 

# processList() 함수 : 데이터 처리 : 오름차순으로 리스트 정렬
# nlist : 리스트다.
def processList(nlist):
    result = None
    result = sorted( nlist ) # 오름차순으로 리스트를 정렬한다.
    return result 

# printList() 함수 : 데이터 출력
# nlist : 리스트다.
def printList(nlist):
    result = None
    for i in nlist:
        str = "성적 : %s" % i
        print( str )
    return result 

# main() 함수 : 프로그램 시작
# 작업 내용
# 1. 데이터 수집 ==> readList() 함수 사용
# 2. 데이터 처리 ==> processList() 함수 사용
# 3. 데이터 출력 ==> printList() 함수 사용
def main():
    result = None

    result = readList() # 리스트가 반환됨. result 는 리스트다. 
    result = processList( result ) 
    result = printList( result )

    return result

# 이 모듈이 단독으로 사용되면 main()를 호출하라.
if __name__ == "__main__":
    main()
