import math

# 몫과 나머지 구하기
num = 5 / 2
print(num)  # (출력값) 2 .5

# 몫을 구하시오
quotient = 5 // 2
print("// 몫은: ", quotient)  # (출력값)

# 몫을 구하시오
quotient = math.floor(num)
print("floor 몫은: ", quotient)  # (출력값)

# 몫을 구하시오. 
# trunc 는 양수일 때는 OK. 음수이면 오류.
quotient = math.trunc(num)
print("trunc 몫은: ", quotient)  # (출력값)

# 나머지를 구하시오
remainder = 5 % 2
print("나머지는 : ", remainder)  # (출력값)
