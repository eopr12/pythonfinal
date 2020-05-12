# GUI 모듈
#   turtle
#   tkinter <-- 리눅스 tk/tcl 언어를 파이썬으로 포팅

import tkinter.filedialog.askopenfilename
import tkinter.filedialog.asksaveasfilename

readFile = tkinter.filedialog.askopenfilename() # 절대 경로 표시되는 파일명.

def main( ) :
    # 파일의 존재 여부 체크
    if readFile != None : 
        # 파일열기
        infile = open(readFile, "r", encoding="UTF-8")

        # 파일 처리
        for line in infile.readlines():
            line = line.strip() # .strip() 양쪽에 공백 제거.
            print(line) # 표준(모니터) 출력

        # 파일 닫기
        infile.close()
    else :
        print("파일 없음")

if __name__ == "__main__":
    main()
