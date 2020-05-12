# 딕셔너리 연산자
# +	        결합 연산자 : X
# *	        반복 연산자 : X
# []	    선택 연산자
# [:]	    범위 선택 연산자
# == 	    일치 연산자
# del	    삭제 연산자
# in        in 연산자
# not in    not in 연산자


# 딕셔너리 선언
dict1 = {"a": 1, "b": "가", "c": "0101"}
dict2 = {"a": 2, "d": "017"}
print("dict1 : ", dict1)
print("dict2 : ", dict2)
print()


# 딕셔너리 in 연산자
array = [1, 2, 3, 4, 5, 6]
print("array: ", array)
print("딕셔너리 in 연산자  1 in array  :", 1 in array)    # True
print("딕셔너리 in 연산자  2 in array  :", 2 in array)    # False
print("딕셔너리 in 연산자  11 in array :", 11 in array)   # False
print("딕셔너리 in 연산자  12 in array :", 12 in array)   # True
print()

## 딕셔너리 not in 연산자
array = [1, 2, 3, 4, 5, 6]
print("array: ", array)
print("딕셔너리 not in 연산자  1  not in array  :", 1 not in array)  # True
print("딕셔너리 not in 연산자  2  not in array  :", 2 not in array)  # False
print("딕셔너리 not in 연산자  11 not in array :", 11 not in array)  # False
print("딕셔너리 not in 연산자  12 not in array :", 12 not in array)  # True
print()


# del 연산자 : 딕셔너리 요소 제거
list_a = [1, 2, 3, 4, 5, 6]
print("array:", list_a)
del list_a[1]
print("del array[1]:", list_a)

list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]
print("del list_b[3:6] >> ", list_b)

list_c = [0, 1, 2, 3, 4, 5, 6]
del list_c[:3]
print("del list_c[:3] >> ", list_c)

list_d = [0, 1, 2, 3, 4, 5, 6]
del list_d[3:]
print("del list_d[3:] >>", list_d)
