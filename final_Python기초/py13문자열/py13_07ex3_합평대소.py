# 문자열 "74 874 9883 73 9 73646 774"  에서 각 숫자의 
# 합계, 평균, 최대값 그리고 최소값을 구하시오.
# 
# a. 문자열 자르기 --> 리스트를 얻게 됨.
# b. 문자열을 정수 리스트로 만든다.
# c. 정수리스트를 오름차순 정렬하시오
# d. 정수리스트의 합계, 평균, 최대값 그리고 최소값을 구하시오.
# 	 합계 함수: sum(), 최대함수: max(), 최소함수: min()       
#    평균 구하는 함수는  만들어야 한다.
#
# ※ 프로그램의 시작점은 main() 메서드가 되도록 만든다.
# ※ 프로그램을 최대한 작은 조각으로 분리하여 작성한다.


def main():
    temp3 = "74 874 9883 73 9 73646 774"
	
	# 여기부터 코드 작성

    # a. 문자열 자르기 --> 리스트를 얻게 됨.
    lst = temp3.split(" ") # ["74","874","9883","73","9","73646","774"]
    print( type(lst), lst ) # 문자열 리스트 

    # lst의 값을 출력 
    # lst의 방번호는 0번 부터 시작한다
    print( lst[0] ,type( lst[0] ) ) # "74" <class 'str'>
    print( lst[1] ,type( lst[1] ) ) # "874" <class 'str'>
    print( lst[2] ,type( lst[2] ) ) # "9883" <class 'str'>
    print( max( lst) ) # 9883

    # b. 문자열을 정수 리스트로 만든다. 
    lst[0] = int( lst[0] ) # 
    lst[1] = int( lst[1] ) # 
    lst[2] = int( lst[2] ) # 
    print( lst[0] ,type( lst[0] ) ) # 74 <class 'int'>
    print( lst[1] ,type( lst[1] ) ) # 874 <class 'int'>
    print( lst[2] ,type( lst[2] ) ) # 9883 <class 'int'>

    for i in range(0, len(lst), 1 ):
        lst[i] = int( lst[i] ) # 
    print( type(lst), lst ) # 정수 리스트. [74,874,9883,73,9,73646,774]

    # c. 정수리스트를 오름차순 정렬하시오
    lst = sorted( lst ) # [9,73,74,774,874,9883,73646]

    # d. 정수리스트에서 합계, 평균, 최대값 그리고 최소값을 구하시오. 
    print( "길이", len(lst) )
    print( "최대값", max( lst) ) # 73646 
    print( "최소값", min( lst) ) # 9 
    print( "합계"  , sum( lst) ) # ????
    print( "평균"  , sum( lst) / len(lst) ) # ????

if __name__ == "__main__" :
    main() 