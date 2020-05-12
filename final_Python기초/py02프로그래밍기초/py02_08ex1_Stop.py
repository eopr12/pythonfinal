# 디버깅을 이용하여 반복 되는 과정을 이해한다.
# F5 / F10 단축 버튼을 사용하시오.
# 주의사항!!! 줄 맞춤

sign = "stop"

while sign == "stop":
    sign = input("현재 신호를 입력하시오: ")  # 여러번 실행된다.
    print("입력값 >>>", sign)

print("OK! 진행합니다.")  # 한번만 실행.
