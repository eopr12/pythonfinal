
# 오류의 종류에 따라서 서로 다른 예외 처리가 가능하다




# An exception flew by!
# Traceback(most recent call last):
#     File "<stdin>", line 2, in < module >
# NameError: HiThere


try:
    raise NameError  # 내장 예외인 NameError 발생
except NameError as ex:
    print("NameError no message", ex)
    # raise


try:
    raise NameError("HiThere")
except NameError as ex:
    print("NameError message", ex)
    #raise
