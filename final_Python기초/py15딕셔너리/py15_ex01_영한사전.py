# 우리는 영한 사전을 구현하여 보자. 어떻게 하면 좋은가? 
# 공백 딕셔너리를 생성하고 여기에 영어 단어를 키로 하고 
# 설명을 값으로 하여 저장하면 될 것이다. 
# 
# 실행 예시)
# 단어를 입력하시오: one 
# 하나
# 단어를 입력하시오: python 
# 없음

english_dict = dict()

english_dict["one"] = "하나"
english_dict["two"] = "둘"
english_dict["three"] = "셋"

word = input("단어를 입력하시오: ");
print (english_dict.get(word, "없음"))
    

