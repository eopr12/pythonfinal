# import 방식
# import 모듈 : import 모듈명 
#               사용방법: 모듈명.함수명
# from import : from 모듈명 import 함수명
#               사용방법: 함수명
# import as : import 모듈명 as aaa
#               사용방법: aaa.함수명

import fibo

# main() 함수 정의 
def main():
    # 사용방법: 모듈명.함수명
    val = fibo.fib2(10)
    print(val)

# 이 모듈이 단독으로 사용되면 main()를 호출하라.
if __name__ == "__main__":
    main()
