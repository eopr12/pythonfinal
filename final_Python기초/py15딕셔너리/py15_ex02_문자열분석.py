# 문자열 안에 있는 문자의 개수, 숫자의 개수, 공백의 개수를 계산하는 프로그램을 작성하여 보자. 
#
# 실행 예시) 
# 문자열을 입력하시오: A picture is worth a thousand words.
# {'digits': 0, 'spaces': 6, 'alphas': 29}


sentence = input("문자열을 입력하시오: ")

table = { "alphas": 0, "digits":0, "spaces": 0 }

for i in sentence:
   if i.isalpha():
      table["alphas"] += 1
   if i.isdigit():
      table["digits"] += 1
   if i.isspace():
      table["spaces"] += 1

print(table)
