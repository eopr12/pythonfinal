
############################
# 리스트에 담을 수 있는 것은? ==> 다
# 리스트의 CRUD2S
# 리스트 선언 ==> [] , list()
# 리스트 추가(C) ==> .append(), .insert()
# 리스트 읽기(R) ==> [방번호]
# 리스트 수정(U) ==> [방번호] = 값
# 리스트 삭제(D) ==> .pop()
# 리스트 정렬(S) ==> .sort() , sorted()
# 리스트 검색(S) ==> 반복문
# 리스트 길이    ==> len()
# 리스트 열거    ==> for 문
############################


############################
# 리스트 선언
# 리스트에는 다 담을 수 있다.
############################
array = []
array = list()
array = [None, 1, 1.1, "문자열", True, [1, 2, 3], {"a": 1}]

############################
# 리스트 전체 출력
############################
print(array)
print("--------------")


############################
# 리스트 요소 출력. [] 선택 연산자를 사용한다.
# 리스트의 시작은 0번부터다.
############################
array = [None, 1, 1.1, "문자열", True, [1, 2, 3], {"a": 1}]
print("array[0] =", array[0], type(array[0]))  # None, <class 'NoneType'>
print("array[1] =", array[1], type(array[1]))  # 1, <class 'int'>
print("array[2] =", array[2], type(array[2]))  # 1.1, <class 'float'>
print("array[3] =", array[3], type(array[3]))  # "문자열", <class 'str'>
print("array[4] =", array[4], type(array[4]))  # True, <class 'bool'>
print("array[5] =", array[5], type(array[5]))  # [1,2,3] , <class 'list'>
print("array[6] =", array[6], type(array[6]))  # {a:1}, <class 'dict'>
print("--------------")


############################
# 리스트 요소 대입
# 리스트의 0번 값을 문자열 "변경"값으로 바꾸시오.
############################
print("array[0] = ", array[0])  # 1
array[0] = "변경"
print("array[0] = ", array[0], type(array[0]))  # 변경, <class 'str'>
print(array)
print("--------------")


############################
# 리스트 요소 추가: C. create
#  추가 : 리스트의 마지막에 넣는다. --> .append() 메서드 사용
#  삽입 : 리스트의 중간에 넣는다.   --> .insert() 메서드 사용
############################
array = [None, 1, 1.1, "문자열", True, [1, 2, 3], {"a": 1}]
print(array)
# [None, 1, 1.1, "문자열", True, [1,2,3] , {"a":1} , "추가"]
array.append("추가")
print(array)
# ["삽입", None, 1, 1.1, "문자열", True, [1,2,3] , {"a":1} , "추가"]
array.insert(0, "삽입")
print(array)
print("--------------")


############################
# 리스트 요소 삭제: D. delete
#  메서드 방식 --> pop() 메서드 . 추천
#  연산자 방식 --> del. 비추천
# 리스트에서 0번을 삭제하시오.
############################
array = [None, 1, 1.1, "문자열", True, [1, 2, 3], {"a": 1}]
array.pop(0)
print(array)  # [1, 1.1, "문자열", True, [1,2,3] , {"a":1} ]
print("--------------")


############################
# 리스트 정렬
############################
array = ["A", "a", "b", "B"]
array.sort()
print(array)  # ['A', 'B', 'a', 'b']
array = ["C", "a", "b"]
array.sort()
print(array)  # ['C', 'a', 'b']
print("--------------")



############################
# 리스트 검색
############################
array = ["A", "a", "b", "B", "A", "a", "b", "B"]
slist = []
for i in range(0, len(array), 1):
    if array[i] == "a":
        slist.append(i)
    else:
        pass
print(slist)  # [1, 5]
print("--------------")


############################
# 리스트 열거
############################
array = ["A", "a", "b", "B", "A", "a", "b", "B"]
for i in array:
    print(i, end=" , ")
print()
print("--------------")
