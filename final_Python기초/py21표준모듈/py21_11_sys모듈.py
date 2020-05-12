
# 모듈을 읽어 들입니다.
import sys
print(sys.argv)

# C:/Python/Mymodules>python py12_09_sys모듈.py you need python
# ['py12_11_sys모듈.py', 'you', 'need', 'python']


# 모듈을 읽어 들입니다.

# 명령 매개변수를 출력합니다.
print(sys.argv)
print("---")

# 컴퓨터 환경과 관련된 정보를 출력합니다.
print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

# 프로그램을 강제로 종료합니다.
sys.exit()
