# 매개변수로 불린,숫자,문자열 자료형을 넘기면 원본은 바뀌지 않는다
# 기본형 매개변수는 원본값 불변 
# 참조형 매개변수는 원본값 변경 

def swap( list1 ):
    # a-->list1[0]
    # b-->list1[1]
    temp = list1[1]
    list1[1] = list1[0]
    list1[0] = temp
    print('swap 안: list1[0]=',list1[0], ', list1[1]=', list1[1])


def main():
    # 리스트 만들기 
    list1 = [5,3]  

    print('swap 전: list1[0]=', list1[0], ', list1[1]=', list1[1])
    swap(list1)
    print('swap 후: list1[0]=', list1[0], ', list1[1]=', list1[1])

main()