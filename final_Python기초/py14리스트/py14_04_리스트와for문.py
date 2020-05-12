# 리스트의 선언
numbers = []

# 리스트에 값을 대입
numbers = [0, 1, 2, 3, 4, 5]

# for문을 사용하여 리스트에 값을 대입
for i in range(0, 5, 1):
    numbers[i] = i * 10
print(numbers)

# 표준입력 리스트에 저장하기
numbers = []
for i in range(10):
    numbers.append(int(input("성적을 입력하시오:")))
print(numbers)

# for문을 사용하여 리스트의 값 출력
for i in numbers:
    print(i)

# 리스트와 for 문
for i in range(0, len(numbers)-1, 1):
    val = numbers[i]
    print(val)

# 문자열과 for 문
for character in "안녕하세요":
    print("-", character)
