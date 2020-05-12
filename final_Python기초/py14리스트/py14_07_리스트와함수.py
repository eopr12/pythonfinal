# 리스트 함수
# len() 	    길이를 구하는 함수
# sorted()	    오름차순 정렬
# min()	        리스트에서 가장 작은 요소 찾기
# max()      	리스트에서 가장 큰 요소 찾기
# .append()	    리스트의 마지막에 요소 추가
# .insert()	    리스트의 특정 위치에 요소 삽입
# .extend()	    리스트 합치기
# .pop()   	    인덱스로 요소 삭제. del 연산자와 동일 효과
# .remove()	    값으로 요소 삭제
# .index()	    값으로 요소 인덱스 찾기
# .sort()	    리스트 오름차순 정렬
# .reverse()	리스트 거꾸로 뒤집기
# .count()	    리스트에 해당 값의 요소 개수
# .clear() 	    모든 요소 삭제


# len() 	    길이를 구하는 함수
a = [1, 3, 2]
len(a)
print("len", len(a))  # 3

# sorted()	    오름차순 정렬
a = ["a", "c", "b", "e", "d"]
sorted(a)
print("sorted", sorted(a))  # ["a","c","b","d"]

# min()	        리스트에서 가장 작은 요소 찾기
a = ["a", "c", "b", "e", "d"]
min(a)
print("min", min(a))  # "a"

# max()      	리스트에서 가장 큰 요소 찾기
a = ["a", "c", "b", "e", "d"]
max(a)
print("max", max(a))  # "e"

# .insert()	    리스트의 특정 위치에 요소 삽입
a = [1, 3, 2]
a.insert(1, 4)
print("insert", a)  # [1,4,3,2]

# .append()	    리스트의 마지막에 요소 추가
a = [1, 3, 2]
a.append(4)
print("append", a)  # [1,3,2,4]

a.insert(len(a), 4)
print("insert", a)  # [1,3,2,4,4]

# .extend()	    리스트 합치기
a = [1, 3, 2]
b = [4, 6, 5]
a.extend(b)
print("extend", a)  # [1,3,2,4,6,5]

# .pop()   	    인덱스로 요소 삭제. del 연산자와 동일 효과
a = ["a", "c", "b", "e", "d"]
a.pop(3)
print("pop", a)  # ["a","c","b","d"]

# .remove()	    값으로 요소 삭제
a = [1, 3, 2, 1, 3, 2]
a.remove(3)
print("remove", a)  # [1,2,1,3,2]

# .index()	    값으로 요소 인덱스 찾기
a = [1, 3, 2]
a.index(3)
print("index", a.index(3))  # 1

# .sort()	    리스트 오름차순 정렬
a = [1, 3, 2]
a.sort()
print("sort", a)  # [1,2,3]

# .reverse()	리스트 거꾸로 뒤집기
a = [1, 3, 2]
a.reverse()
print("reverse", a)  # [2,3,1]

# .count()	    리스트에 해당 값의 요소 개수
a = ["a", "c", "b", "e", "b"]
a.count("b")
print("count", a.count("b"))  # 2

# .clear() 	    모든 요소 삭제
a = [1, 3, 2]
a.clear()
print("clear", a)  # []
