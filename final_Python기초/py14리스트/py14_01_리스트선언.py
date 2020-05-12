
############################
# 리스트 선언
# 리스트에는 다 담을 수 있다.
############################

# 리터럴로 공백 리스트 생성
list1 = []
print(list1, type(list1))  # [] <class 'list'>

# 함수로 공백 리스트 생성
list2 = list()
print(list2, type(list2))  # [] <class 'list'>

# 리스트에는 다 담을 수 있다.
list3 = [None, 1, 1.1, "문자열", True, [1, 2, 3],  {"a": 1}]
print(list3, type(list3))  # [None, 1, 1.1, '문자열', True, [1, 2, 3], {'a': 1}]

# 리스트에는 함수도 담을 수 있다.


def func():
    print("출력")


list4 = [None, 1, 1.1, "문자열", True, [1, 2, 3],  {"a": 1}, func]
# [None, 1, 1.1, '문자열', True, [1, 2, 3], {'a': 1}, <function func at 0x033888E8>] <class 'list'>
print(list4, type(list4))
list4[-1]()  # func( ) 함수 호출과 같음.


# 문자 H, e, l, l, o를 요소로 가지는 리스트
list1 = ["H", "e", "l", "l", "o"]
print(list1, type(list1))  # ['H', 'e', 'l', 'l', 'o'] <class 'list'>

# 문자열을 리스트로 변환.
# 문자열 "Hello"를  H, e, l, l, o를 요소로 가지는 리스트 변환
list2 = list("Hello")
print(list2, type(list2))  # ['H', 'e', 'l', 'l', 'o'] <class 'list'>

# 문자열 Hello를 요소로 가지는 리스트
list3 = ["Hello"]
print(list3, type(list3))  # ['Hello] <class 'list'>

# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
list4 = [0, 1, 2, 3, 4]
print(list4, type(list4))  # [0, 1, 2, 3, 4] <class 'list'>

# 시퀀스를 이용하여 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
list5 = list(range(0, 5, 1))
print(list5, type(list5))  # [0, 1, 2, 3, 4] <class 'list'>
