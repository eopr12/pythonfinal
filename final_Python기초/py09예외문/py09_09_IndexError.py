
# 오류의 종류에 따라서 서로 다른 예외 처리가 가능하다

# IndexError 예외
# Traceback (most recent call last):
#   File ".\py09_09_IndexError.py", line 3, in <module>
#     print("안녕하세요"[10])
# IndexError: string index out of range


try:
    array = [1, 2, 3]
    print(array[3])  # IndexError

    # 출력합니다.
    print("# IndexError 예외")
    print("안녕하세요"[10])
except Exception as ex:
    print("Exception",  ex)  # 로그 파일에 저장하는 방식으로 수정 필요
