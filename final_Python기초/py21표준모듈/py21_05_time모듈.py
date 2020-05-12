#################################
# time 모듈의 사용법을 익힌다.
#
# time.time()       unix 타임을 반환 한다. 1970.01.01 00:00:00 부터 경과된 시간 
# time.sleep(초)	동작 중인프로세스를 주어진 초만큼 정지
#################################

# 모듈을 읽어 들입니다.
import time
import datetime

pritn( time.time() ) # 1461203464.6591916


print(datetime.datetime.now(), "지금부터 5초 동안 정지합니다!")
time.sleep(5)
print(datetime.datetime.now(), "프로그램을 종료합니다")
