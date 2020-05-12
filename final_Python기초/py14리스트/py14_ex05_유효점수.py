
###################################
# 심사 위원의 점수를 입력하여 유효 점수와 평균을 출력하는 프로그램을 작성합니다.
# 유효점수는 최고점과 최저점을 제외한 점수이며 합계와 평균은 유효점수로 계산합니다.
# 유효점수 합계 구하는 부분을 함수를 이용하시오.
# 평균 구하는 부분을 함수를 이용하시오.
# 평균은 소수점 두 자리까지만 출력하시오.
#
#
# ▪ 실행결과예시
# 심사 위원 수를 입력하시오 :  5
# 심사 위원 점수 입력 :  7
# 심사 위원 점수 입력 :  9
# 심사 위원 점수 입력 :  4
# 심사 위원 점수 입력 :  8
# 심사 위원 점수 입력 :  5
# 유효점수 : 5  7  8
# 합계 : 20
# 평균 : 6.67
#
#
# . 심사 위원수를 입력 받는다.
# . 심사 위원의 점수 입력 받아서 "점수리스트"에 저장.
#   몇 번 입력 받아야 하는가? 심사 위원수 만큼
# . 리스트 정렬하기.
# . 1번방부터 마지막방 -1 까지 합계를 구하는 메서드 만들기
# . 평균을 구하는 메서드 만들기.
# . 합계를 구하고 출력한다.
# . 평균을 구하고 출력한다.
###################################


def getList():
    result = None

    try:
        심사위원수 = input("심사 위원 수를 입력하시오 : ")
        심사위원수 = int(심사위원수)

        result = []
        for i in range(0, 심사위원수, 1):
            성적 = input("심사 위원 점수 입력 : ")
            성적 = int(성적)
            result.append(성적)

    except Exception as ex:
        print("getList 예외", ex)
        pass

    return result


def getSum(리스트):
    result = None

    try:
        result = sum(리스트)
    except Exception as ex:
        print("getSum 예외", ex)

    return result


def getAvg(리스트):
    result = None

    try:
        합계 = sum(리스트)
        result = 합계 / len(리스트)
    except Exception as ex:
        print("getAvg 예외", ex)

    return result


def printScore(리스트):
    print("유효 점수 : ", end="")
    for i in 리스트:
        print(i, end=", ")
    print()


def main():
    # 점수 입력 받기
    입력점수리스트 = getList()
    # 정렬 리스트 만들기
    입력점수리스트.sort()
    # 유효점수 리스트 만들기
    입력점수리스트.sort()
    유효점수리스트 = 입력점수리스트[1:-1]
    # 유효점수 출력
    printScore(유효점수리스트)
    합계 = getSum(유효점수리스트)
    print("합계 : %s " % 합계)
    평균 = getAvg(유효점수리스트)
    print("평균 : %.2f " % 평균)


if __name__ == "__main__":
    main()
