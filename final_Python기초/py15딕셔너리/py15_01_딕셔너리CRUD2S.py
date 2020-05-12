
# 딕셔너리의 CRUD2S 사용법을 익힌다. 
# 딕셔너리에 담을 수 있는 것은? ==> 다
# 딕셔너리 선언 ==>  dic = { }
# 딕셔너리 추가(C) ==> dic["key값"] = "값"  <== 없으면 만든다.
# 딕셔너리 읽기(R) ==> dic["key값"]
# 딕셔너리 수정(U) ==> dic["key값"] = "값"  <== 있으면 바꾼다.
# 딕셔너리 삭제(D) ==> dic.pop("key값")
# 딕셔너리 정렬(S) ==> 없음. 왜냐하면 순서가 없기 때문
# 딕셔너리 검색(S) ==> 반복문 
# 딕셔너리 길이    ==> len(dic.keys() ) , len(dic.values() ) , 


# 딕셔너리 선언하기
사전  = {
    "name" : "망고",
    "type" : "당" ,
    "ingredient" : ["망고", "설탕", "소금", "치즈"] ,
    "origin": "필리핀" ,
}

# 딕셔너리 전체 내용을 출력해봅니다.
print( 사전 )


# R: 요소 추가 전에 내용을 출력해봅니다.
# 1. 선택 연산자를 사용하는 방법. name, type 의 값을 출력
# 2. get() 메서드를 사용하는 방법. ingredient, origin 의 값을 출력
print( 사전["name"] ) # key=name 방의 값을 출력 
print( 사전["type"] ) # key=type 방의 값을 출력 
print( 사전.get("ingredient") ) # key=ingredient 방의 값을 출력 
print( 사전.get("origin") ) # key=ingredient 방의 값을 출력


# C: 딕셔너리 추가
# 사전 의 key 에 head를 value에는 body 를 추가하고 값을 출력하시오 
사전["head"] = "body"
print( 사전 )
print( 사전["head"] ) # key=head 방의 값을 출력. 선택 연산자 [] 로 읽기 
print( 사전.get("head") ) # key=head 방의 값을 출력. get() 메서드로 읽기




# U: 딕셔너리 수정
# name 값을 "8D 망고" 로 수정하시오.
print( "수정 전", 사전["name"] ) # key=name 방의 값을 출력. "망고" 출력
사전["name"] = "8D 망고" 
print( "수정 후", 사전["name"] ) # key=name 방의 값을 출력. "8D 망고" 출력


# D: 딕셔너리 삭제.
# 1. 연산자 방식 ==> del . 비추천
# 2. 메서드 방식 ==> .pop("key"). 추천
# name, type 키를 삭제
print( "삭제 전", 사전 )
사전.pop( "name") # 방이름 : name 을 삭제 
사전.pop( "type") # 방이름 : type 을 삭제 
print( "삭제 후", 사전 )



###################
# S: 정렬. 딕셔너리는 정렬하는 방법이 없다. 
#  ==> 왜냐하면 순서(방번호)가 없기 때문에.
# key 만 정렬. keys() 메서드 사용.
# 단, key 값들만 정렬하는 것은 가능하다. 
#  ==> 왜냐하면 key 값들만 있으면 리스트로 처리 가능이기 때문
# value 만 정렬. values() 메서드 사용.
# 단, value 값들만 정렬하는 것은 가능하다. 
#  ==> 왜냐하면 value 값들만 있으면 리스트로 처리 가능이기 때문
keys  =  list( 사전.keys() ) # keys는 리스트다. 
print("keys 정렬 전", keys) # keys 정렬 전 ['ingredient', 'origin', 'head']
keys.sort()
print("keys 정렬 후", keys) # keys 정렬 후 ['head', 'ingredient', 'origin']

values  = list( 사전.values() ) # values 는 리스트다. 
print("values 정렬 전", values) # values 정렬 전 [['망고', '설탕', '소금', '치즈'], '필리핀', 'body']
values.sort() # 에러가 정상. 왜냐하면 타입이 다르기 때문에.
print("values 정렬 후", values)


###################
# S: 검색. 특별한 방법이 없다. 반복문을 사용하여 반복한다.
# 선택연산자를 사용하면 바로 검색 되기 때문. 사전["name"]




# 존재하지 않는 키: 선택 연산자로 없는 키에 접근하면 에러 발생.
# 1. 선택 연산자를 사용하는 읽기 방법. 
# 2. get() 메서드를 사용하는 읽기 방법. 
# try ~ except 를 추가하시오.  
# KeyError
try:
    name = 사전["name"]  # "사전"에는 name 키값이 없어서 에러가 난다.
except KeyError as ex:
    print( "KeyError", ex )
except Exception as ex:
    print( "Exception", ex )


	
# 존재하지 않는 키에 접근하면 에러 발생. try ~ except 를 추가하시오.  
# 딕셔너리에서 키의 존재 여부 확인.  
# 방법1. get() 메서드 사용하는 방법
#       get() 메서드 키가 존재하지 않는 경우에  None을 반환한다. 
# 방법2. in 연산자를 사용하는 방법


# 방법1. get() 메서드 사용하는 방법
#       vaule 값이 None 이면 키가 없다는 의미다.

# get() 메서드는 "사전"에는 name 키값이 없어도 에러가 안난다. 없으면 None 으로 반환된다. 
name = 사전.get("name")    
print("name", name) 


# 방법2. in 연산자를 사용하는 방법
if "name" in 사전:
    print( "키 있음")
    name = 사전["name"]  # "사전"에는 name 키값이 없어서 에러가 난다.
else :
    print( "키 없음")
    name = None 
print("name", name) 



###################
# 딕셔너리 열거
# key 만 열거. keys() 메서드 사용.
# value 만 열거. values() 메서드 사용.
# key 와 value를 쌍으로 열거. items() 메서드 사용.
##################

# 딕셔너리 열거
for i in 사전:
    print("사전열거", i, 사전[ i ]) # i 는 키값(방이름), 사전[ i ] 는 방의값.

# 리스트 열거
for i in [1,2,3,4]:
    print("리스트열거", i) # i 는 방의값 이다.

# key 만 열거. keys() 메서드 사용.
for i in 사전.keys():
    print("keys() >> ", i) # i 는 키값(방이름) 이다. 

# value 만 열거. values() 메서드 사용.
for i in 사전.values():
    print("values() >> ", i) # i 는 value값(방의값) 이다. 

# key, value를 쌍으로 열거. items() 메서드 사용.
for i in 사전.items():
    print("items() >>", i, type(i) ) # i 는 튜플(읽기전용 리스트) 이다. 
    print("items() >>", i[0], i[1]) # i 는 튜플(읽기전용 리스트) 이다. 



###################
# 딕셔너리 정렬
# key 만 정렬. keys() 메서드 사용.
keys  =  list( 사전.keys() ) # keys는 리스트다. 
print("keys 정렬 전", keys) # keys 정렬 전 ['ingredient', 'origin', 'head']
keys.sort()
print("keys 정렬 후", keys) # keys 정렬 후 ['head', 'ingredient', 'origin']

# value 만 정렬. values() 메서드 사용.
values  = list( 사전.values() ) # values 는 리스트다. 
print("values 정렬 전", values) # values 정렬 전 [['망고', '설탕', '소금', '치즈'], '필리핀', 'body']
values.sort() # 에러가 정상. 왜냐하면 타입이 다르기 때문에.
print("values 정렬 후", values)