# py02_09ex1_Salary

# 변수 선언 : salary , deposit 변수(메모리 공간) 선언
salary = 0 
deposit = 0

# 숫자를 입력(키보드 입력 == 표준입력) 받고(이것은 문자열)
#  salary 변수 에 저장하시오(넣으시오).
# input으로 입력 받은 숫자는 정수인가 문자열인가? 문자열
salary = input( "월급을 입력하세요")

#문자열을 정수로 바꾼다. ==> 형변환. int()
salary = int( salary )

# 10년치 월급의 총합을 구하고 그 값을 deposit 에 저장.
deposit = 10 * 12 * salary

# 10년 동안의 저축액: ?????  원 형태로 출력(모니터출력, 표준출력)하시오.
print( "10년 동안의 저축액: ", deposit , " 원")


