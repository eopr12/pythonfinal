
#########################
# 키보드 입력을 파일에 쓰는 프로그램을 작성하여 본다.
# 한 행씩 읽어 ==> input() 함수 
# 파일에 쓰기 ==> writeline() 함수
#########################

import os

# 파일 열기
pfw = open("phones.txt", "a", encoding="utf-8")

# 키보드 입력 받고 파일에 쓰기
입력값 = input("입력하세요>>> ")
pfw.write( 입력값 ) # write() 줄바꿈이 안된다. 어떻게 ?
pfw.write( "\n" )

입력값 = input("입력하세요>>> ")
pfw.write( 입력값 ) # write() 줄바꿈이 안된다. 어떻게 ?
pfw.write( "\n" )

입력값 = input("입력하세요>>> ")
pfw.write( 입력값 ) # write() 줄바꿈이 안된다. 어떻게 ?
pfw.write( "\n" )


# 파일 닫기
pfw.close()


########################################
# 반복문을 사용하는 방법으로 바꾸기
########################################

# 파일 열기
pfw = open("phones.txt", "a", encoding="utf-8")

# 키보드 입력 받고 파일에 쓰기
while True:
        
    입력값 = input("입력하세요. 입력을 끝내려면 엔터>>> ")

    if 입력값 == "":
        break
    else:
        pfw.write( 입력값 ) # write() 줄바꿈이 안된다. 어떻게 ?
        pfw.write( "\n" )


# 파일 닫기
pfw.close()
