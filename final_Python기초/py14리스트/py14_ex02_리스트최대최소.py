# 10개의 정수를 입력 받아 리스트에 저장하고 이 리스트의 최대, 최소값을 구하시오. 
# py13_07ex2.문자열실습2.py 참고
# 
# ※ 프로그램의 시작점은 main() 메서드가 되도록 만든다.
# ※ 프로그램을 최대한 작은 조각으로 분리하여 작성한다.
# a. 문자열 입력 받기
# b. 문자열 자르기 --> 리스트를 얻게 됨.
# c. 문자열을 정수 리스트로 만든다. 
# d. 정수리스트를 오름차순 정렬하시오


# main 함수 정의
def main():    
    # a. 문자열 입력 받기
    정수문자열 = "23 96 35 42 81 19 8 77 50 64"

    # b. 문자열 자르기 --> 리스트를 얻게 됨.
    문자열리스트 = 정수문자열.split(" ") # 문자열 리스트

    # c. 문자열리스트 을 정수리스트로 만든다. 
    # int() 를사용하여 정수로 변환
    정수리스트 = [] 
    for i in 문자열리스트:
        정수 = int( i )# 문자열을 정수로 바꾼다.
        # 정수리스트에 변환된 정수 를 추가
        정수리스트.append(  정수 )

    '''
    for i in range(0, len(문자열리스트), 1):
        정수 = int( 문자열리스트[i] )# 문자열을 정수로 바꾼다.
        # 정수리스트에 변환된 정수 를 추가
        정수리스트.append(  정수 )
    '''

    # d. 정수리스트를 오름차순 정렬하시오
    print("리스트 정렬 전", 정수리스트)
    정수리스트.sort()
    print("리스트 정렬 후", 정수리스트)

    # e. 최대값 구하기
    최대값 = max(정수리스트)
    print( "최대값", 최대값 )

    # f. 최소값 구하기
    최소값 = min(정수리스트)
    print( "최소값", 최소값 )
    

# main 함수 호출
main() 