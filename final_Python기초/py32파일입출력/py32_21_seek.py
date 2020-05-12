

#########################
# 처음부터 10개의 글자 읽기
infile = open("./file/test.txt", "r+")
str = infile.read(10)
print("읽은 문자열 : ", str)

position = infile.tell()
print("현재 위치:  ", position)

position = infile.seek(0, 0)
str = infile.read(10)
print("다시 읽은 문자열 : ", str)
infile.close()

#########################
# 처음부터 10개의 글자 읽기
print("########### read")
infile = open("./file/phones.txt", "r", encoding="UTF-8")
s = infile.read(10)
print(s)
infile.close()


#########################
# 2번째 라인부터 글자 읽기
infile = open("./file/phones.txt", "r", encoding="UTF-8")
s = infile.readline()
print(s)
infile.close()
