# 단축 평가란?
#     조건식을 왼쪽에서 오른쪽으로 진행하면서 참/거짓을 판단
#     식 전체가 자명한 경우, 더 이상 수식을 평가하지 않는 방법
#
# 'and'와 'or'는 단축 평가로 수행되도록 보장
#     x and y : x가 False인 경우, y값은 평가하지 않음
#     x or y : x가 True인 경우, y값은 평가하지 않음
#
# 단축 평가의 장점
#     조건식의 결과가 결정되는 시점 이후로 추가적인 판별 연산을 수행하지 않기 때문에 속도 향상
#     Run time error 발생을 try ~ except 구문이 아닌 논리식으로 사전에 차단 가능


a = 0
if a and 10 / a:
    print("a가 0입니다.")
else:
    print("에러없이 통과")


if bool(a) and 10 / a:
    print("a가 0입니다.")
else:
    print("에러없이 통과")


if a == 0 and 10 / a:
    print("a가 0입니다.")
else:
    print("에러없이 통과")

print("정상 종료")
