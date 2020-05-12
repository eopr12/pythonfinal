
###################################
# 리스트를 이용해서 반의 평균을 구하시오.
#   . 학생수를 입력 받고 학생마다의 성적을 입력 받아 리스트에 저장한다. ==> getList()
#   . 리스트의 합계를 구하고 ==> getSum(리스트)
#   . 출력한다.     ==> print("합계는 : ")
#   . 평균을 구하고 ==> getAvg(리스트)
#   . 출력한다.     ==> print("평균은 : ")
#
# 실행결과예시
#   학생수를 입력하시오: 3
#   성적을 입력하시오: 35
#   성적을 입력하시오: 45
#   성적을 입력하시오: 55
#   합계는 :  135
#   평균은 : 45
###################################


def getList():
    result = None

    try:
        학생수 = input("학생수를 입력하시오: ")
        학생수 = int(학생수)

        result = []
        for i in range(0, 학생수, 1):
            성적 = input("성적을 입력하시오: ")
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


def main():
    학생성적리스트 = getList()
    합계 = getSum(학생성적리스트)
    print("합계는 : ", 합계)
    평균 = getAvg(학생성적리스트)
    print("평균은 : ", 평균)


if __name__ == "__main__":
    main()
