

student1 =  ( "철수" , 19, "CS" )
print( type(student1) ) # <class 'tuple'>

(name, age, major ) = student1
print( name, age, major)

name1, age1, major1 = student1
print( name1, age1, major1)


# 이메일을 입력 받고 @를 기준으로 id와 도메인을 분리하는 프로그램을 작성하시오.
# 예시) abc@naver.com  --> id: abc  , domain: naver.com
이메일 = "abc@naver.com"
(id, domain) = 이메일.split("@") # 양쪽의 갯수가 같아야 한다.
print("이메일", 이메일)
print("id", id)
print("domain", domain)
