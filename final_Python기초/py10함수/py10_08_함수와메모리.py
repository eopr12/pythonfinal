# 함수와 메모리의 관계를 이해한다.

# 함수를 선언하면…
# 힙 메모리에는 함수 객체가 생성
# 스택 메모리에는 함수를 가리키는 레퍼런스가 생성

# 함수 레퍼런스를 통해서 함수를 사용하게 됨
# 함수 레퍼런스는 다른 변수에 할당할 수 있음


def times(a, b):
    return a*b


print("copytimes address: ", id(times))  # 0x????????
print("times: ", times(10, 10))  # 100

copytimes = times
r = copytimes(10, 10)

print("copytimes address: ", id(copytimes))  # 0x????????
print("copytimes: ", r)  # 100
