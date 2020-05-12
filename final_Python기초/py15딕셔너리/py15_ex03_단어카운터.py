# 사용자가 지정하는 파일을 읽어서 파일에 저장된 
# 각각의 단어가 몇 번이나 나오는지를 계산하는 프로그램을 작성하여 보자. 
# 
# 실행 예시)
# 파일 이름: proverbs.txt
# {
#     "a": 1,
#     "done.": 1,
#     "that": 1,
#     "well.": 1,
#     "ends": 1,
#     "Well": 1,
#     "flock": 1,
#     "feather": 1,
#     "All"s": 1,
#     "Birds": 1,
#     "together.": 1,
#     "of": 1,
#     "fast.": 1,
#     "begun": 1,
#     "half": 1,
#     "well": 1,
#     "travels": 1,
#     "news": 1,
#     "is": 1,
#     "Bad": 1,
#  }

fname = input("파일 이름: ")
file = open(fname, "r")

table = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in table:
            table[word] = 1
        else:
            table[word] += 1

print(table)
