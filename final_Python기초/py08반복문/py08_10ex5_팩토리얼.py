# 팩토리얼을 계산하는 프로그램을 작성하여 보자.
# 팩토리얼 n!은 1부터 n까지의 정수를 모두 곱한 것을 의미한다. 
# 즉, n! = 1×2×3×……×(n-1)×n이다. 
# 
# 힌트. 10부터 1까지 -1씩 감소시키면서
# 정수를 입력하시오: 10
# 10 !은 3628800 이다.

입력값 = input("정수를 입력하시오:")
입력값 = int(입력값)

fact = 1
for i in range(1, 입력값+1, 1):
    fact = fact*i

str1 = "%s !은 %s 입니다 " % (입력값, fact)
print(str1)
