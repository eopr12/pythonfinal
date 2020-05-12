
# 문자열에 *, + 연산자가 있다.
# 문자열에는 / 연산자가 없다. 

a = input("정수 입력") # 
b = input("정수 입력") # 

try:
    a = int(a)
    b = int(b)
    avg = (a+b) / 2
except ValueError:
    pass

if avg >= 160 :
    print("합격")
else:
    print("불합격")

