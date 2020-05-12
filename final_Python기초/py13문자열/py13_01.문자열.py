# py02_06_문자열결합
i = 10
j = 20
k = i + j

# 출력  :  더하기 : 10 + 20 = 30
print("더하기: ", i, "+", j, "=", k)

s1 = "Hello"
s2 = " World"
print(s1 + s2)

s3 = s1 + s2
print(s3)

# "abcdefg"에서 문자열 추출 연습하기
str = "abcdefg"
print(str[2:])     # cdefg
print(str[:2])     # ab
print(str[2:3])    # c
print(str[2:6])    # cdef
print(str[:-1])    # abcdef
print(str[-1:])    # g
print(str[-3:-4])
print(str[-3:-1])  # ef
print(str[-3:0])
print(str[-3:])    # efg

# "안녕하세요" 문자열 열거
for character in "안녕하세요":
    print("-", character)

# "apple" 문자열 열거
fruit = "apple"
for letter in fruit:
   print(letter, end=" ") 
