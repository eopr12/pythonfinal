
#########################
##

import os
def getAbsFileName( fileName):
    result = ""
    absfile = os.path.abspath(__file__) # 스크립트 파일의 절대경로
    curDir = os.path.dirname( absfile  ) # 스크립트 폴더의 절대경로
    txtA = os.path.join( "/", fileName ) # ==> "/phones.txt"
    result = os.path.normpath( curDir + txtA ) # ==> 절대경로
    return result

fileName = getAbsFileName("/bb.txt")
pfw = open(fileName, "w", encoding="utf=8")
pfw.write("홍길동 010-1234-5678\n")
pfw.write("김철수 010-1234-5679\n")
pfw.write("김영희 010-1234-5680\n")
pfw.close()