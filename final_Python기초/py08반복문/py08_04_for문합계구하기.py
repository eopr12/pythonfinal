
###########################
# 0부터 10까지의 합계를 구하시오

sum = 0 # 합계를 저장하는 변수
for x in range(0, 11, 1 ):
    sum = sum + x

print("sum = ", sum ) # sum = 45

###########################
# 문제. 0부터 100까지 짝수의 합계를 구하시오
sum = 0
for i in range(0, 101, 2 ):
    sum = sum + i
print(sum) 

sum = 0
for i in range(0, 101, 1 ):
    # i가 짝수이면 sum 하고 아니면 pass
    if i % 2 == 0 :
        sum = sum + i
    else:
        pass
print(sum) 