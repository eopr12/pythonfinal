# 영문자로 구성된 텍스트를 입력받아 영문자 알파벳의 히스토그램을 만들어보자.
# 이 도전 문제는 문자열과 딕셔너리를 다루는 연습을 위한 것이다.
# 단, 대문자와 소문자는 같은 것으로 다룬다.
#
# 2차원 리스트 구조 이해하기
# array[0] == This  ==> 0번방(array[0]) 의 첫글자 <==> array[0][0] == T
# array[1] == was   ==> 1번방(array[1]) 의 첫글자 <==> array[1][0] == w
# array[2] == a     ==> 2번방(array[2]) 의 첫글자 <==> array[2][0] == a


def main():

    str = """This was a great help.
    I applied this method to similiar problem
    and rather than concat a SELECT statement
    I created an event scheduled every couple
    hours to rebuild a view that pivots n amount
    of rows from one table into n columns on the other.
    It is a big help because before I was rebuilding
    the query using PHP on every execution of the SELECT.
    Even though views can not leverage Indexes,
    I am thinking filtering performance will not
    be an issue as the pivoted rows->columns
    represent types of training employees at a
    franchise have so the view will not ever break
    a few thousand rows."""

    str = str.replace("\n", "")
    table = {}
    array = str.split(" ")
    for i in range(0, len(array), 1):
        # print(array[i]) # This, was , a, ...
        # array[0] == This  ==> 0번방(array[0]) 의 첫글자 <==> array[0][0] == T
        # array[1] == was   ==> 1번방(array[1]) 의 첫글자 <==> array[1][0] == w
        # array[2] == a     ==> 2번방(array[2]) 의 첫글자 <==> array[2][0] == a
        if len(array[i]) > 0:
            key = array[i][0]  # 첫번째 글자 추출
            key = key.upper()  # 대문자로 치환
            tmp = table.get(key)  # table에서 키값으로 찾기

            if tmp == None:
                # 미존재
                table[key] = 1  # 숫자로 저장
            else:
                # 존재
                table[key] = table[key] + 1

    # 출력하기. 딕셔너리 키와 값의 쌍으로 열거.
    # items() 메서드 사용. key, value를 쌍으로 열거.
    for item in table.items():
        # item[0] 을 item[1] 번 반복하시오
        # item =  (T, 17) ==> TTTTTTTTTTTTTTTTT
        # item =  (W, 4 ) ==> WWWW
        출력 = "%s %3s   %s" % (item[0], item[1], item[0]*item[1])
        print(출력)


main()
