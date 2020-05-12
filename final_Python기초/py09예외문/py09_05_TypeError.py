
# 오류의 종류에 따라서 서로 다른 예외 처리가 가능하다

# Traceback (most recent call last):
#   File ".\py09_05_TypeError.py", line 4, in <module>
#     string + number
# TypeError: must be str, not int

try:
    string = "문자열"
    number = 273

    string + number
except Exception as ex:
    print( "Exception",  ex ) # 로그 파일에 저장하는 방식으로 수정 필요
