# py07_05_연속if

# 하나의 점수를 입력 받고, 입력 받은 점수에 해당하는 학점을 출력하는 프로그램을 작성하시오.
# 입력 받는 정수는 0~100까지이고    
# 90점 이상이면 A,    
# 80점 이상이면 B,    
# 70점 이상이면 C,   
# 60점 이상이면 D,    
# 나머지는 F

############################
# 비교 연산자와 논리 연산자 결합한 방법

grade = input("점수 :") # 95
score = int(score) # 95
grade = "F"

if 90<= score and score <=100:
    grade = "A"
elif 80 <= score and score <90 :
    grade = "B"
elif 70 <= score and score <80 :
    grade = "C"
elif 60 <= score and score <70 :
    grade = "D"
else: #elif 0<= grade and grade <60  :
    grade = "F"

print("학점: ", grade, "입니다." )



############################
# 비교 연산자만 사용한 방법
score = input("score :") # 95
score = int(score) # 95
grade = "F"

if 90<= score :
    grade = "A"
elif 80 <= score :
    grade = "B"
elif 70 <= score :
    grade = "C"
elif 60 <= score :
    grade = "D"
else:
    grade = "F"

print("학점: ", grade, "입니다." )


######################
# 도전 과제. 
# score 는 0부터 100사이의 값만 가능해야 한다.
# 그 이외의 값이 들어오면 score를 다시 입력 받게 작성하시오.
# 어떻게 처리해야 할까?
######################



score = -1

# score 는 0부터 100사이의 값만 가능해야 한다.
while score<0 or 100 < score :
    # 그 이외의 값이 들어오면 score를 다시 입력 받게 작성하시오.
    score = input("score :") # 95
    score = int(score) # 95

    if 0<= score <= 100:
        # 반복문을 종료
        break
    else:
        # 다시 입력 받는다.
        pass

grade = ""

if 90<= score :
    grade = "A"
elif 80 <= score :
    grade = "B"
elif 70 <= score :
    grade = "C"
elif 60 <= score :
    grade = "D"
else:
    grade = "F"

print("학점: ", grade, "입니다." )