
# 파이썬에서 변수는 어떤 데이터든지 저장할 수 있다.
# 파이썬에서는 모든 것이 객체로 처리된다.

a = 3
b = a
print("value >> ", a, b)
print("reference address >> ", id(a), id(b))
print("실제값 일치 여부 확인 >> ", a == b)  # 일치 연산자 : 실제값 일치 여부 확인
print("주소값 일체 여부 확인 >> ", id(a) == id(b))  # 일치 연산자 : 주소값 일체 여부 확인
print("is 연산자 >> ", a is b)  # is 연산자

print()
print()


a = 1000
b = a
print("value >> ", a, b)
print("reference address >> ", id(a), id(b))
print("실제값 일치 여부 확인 >> ", a == b)  # 일치 연산자 : 실제값 일치 여부 확인
print("주소값 일체 여부 확인 >> ", id(a) == id(b))  # 일치 연산자 : 주소값 일체 여부 확인
print("is 연산자 >> ", a is b)  # is 연산자

print()
print()

a = 1000.01
b = a
print("value >> ", a, b)
print("reference address >> ", id(a), id(b))
print("실제값 일치 여부 확인 >> ", a == b)  # 일치 연산자 : 실제값 일치 여부 확인
print("주소값 일체 여부 확인 >> ", id(a) == id(b))  # 일치 연산자 : 주소값 일체 여부 확인
print("is 연산자 >> ", a is b)  # is 연산자
