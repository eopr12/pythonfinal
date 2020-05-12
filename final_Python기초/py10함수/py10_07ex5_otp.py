# 사용자 함수 만들기
# 일회용 패스워드 생성기를 이용하여서 3개의 패스워드를 생성하여 출력하는 프로그램을 작성해보자. 

import random


def genPass():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""

    for i in range(6):
        index = random.randrange(len(alphabet))
        password = password + alphabet[index]
    return password


print(genPass())
print(genPass())
print(genPass())