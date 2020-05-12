# 리스트 연산자
# +	        결합 연산자
# *	        반복 연산자
# []	    선택 연산자
# [:]	    범위 연산자
# == 	    일치 연산자
# in        in 연산자
# not in    not in 연산자
# del	    삭제 연산자


# 리스트 선언
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("list1 : ", list1)
print("list2 : ", list2)
print()

# 리스트 + 연산자
list3 = list1 + list2  # [1, 2, 3, 4, 5, 6]
print(" 리스트 + 연산자 ", list3)
print()

# 리스트 * 연산자
list4 = list1 * 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(" 리스트 * 연산자 ", list4)
print()

# 선택 연산자

# 범위 연산자

# 일치 연산자

# 리스트 in 연산자
array = [1, 2, 3, 4, 5, 6]
print("array: ", array)
print("리스트 in 연산자  1 in array  :", 1 in array)    # True
print("리스트 in 연산자  2 in array  :", 2 in array)    # False
print("리스트 in 연산자  11 in array :", 11 in array)   # False
print("리스트 in 연산자  12 in array :", 12 in array)   # True
print()

## 리스트 not in 연산자
array = [1, 2, 3, 4, 5, 6]
print("array: ", array)
print("리스트 not in 연산자  1  not in array  :", 1 not in array)  # True
print("리스트 not in 연산자  2  not in array  :", 2 not in array)  # False
print("리스트 not in 연산자  11 not in array :", 11 not in array)  # False
print("리스트 not in 연산자  12 not in array :", 12 not in array)  # True
print()

# del 연산자 : 리스트 요소 제거
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
