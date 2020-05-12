
# 오류의 종류에 따라서 서로 다른 예외 처리가 가능하다


#  OSError


import sys

try:
    f = open("myfile.txt")
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
