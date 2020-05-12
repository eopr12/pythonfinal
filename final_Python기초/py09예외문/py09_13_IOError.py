
# 오류의 종류에 따라서 서로 다른 예외 처리가 가능하다


try:
    fname = input("파일 이름을 입력하세요: ")
    infile = open(fname, "r") 
except IOError:
    print("파일 " + fname + "을 발견할 수 없습니다.")


try:
   fh = open("testfile", "w")
   fh.write("테스트 데이터를 파일에 씁니다!!")
except IOError:
   print("Error: 파일을 찾을 수 없거나 데이터를 쓸 수 없습니다. ")
else:
   print("파일에 성공적으로 기록하였습니다. ")
   fh.close()

try:
   f = open("test.txt", "w" )
   f.write("테스트 데이터를 파일에 씁니다!!")
   # 파일 연산을 수행한다. 
except IOError:
   print("Error: 파일을 찾을 수 없거나 데이터를 쓸 수 없습니다. ")
finally:
   f.close()
