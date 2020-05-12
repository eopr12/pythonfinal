#######################
# fibo 모듈 만들기 
#######################

# fib(n) : 피보나치 수열의 결과를 반환하는 함수 만들기 
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

# fib2(n) : 피보나치 수열을 리스트로 반환하는 함수 만들기 
def fib2(n): 	
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if  __name__ == "__main__" :
    import sys  # 명령 프롬프트에서 인자 받을 때 사용.
    fib( int( sys.argv[1] ) )	

