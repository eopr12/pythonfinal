# 조건식의 참/거짓 판단은 기본적으로 자료형의 bool 값과 동일
# True로 판명 : 10 > 0
# False로 판명 : 5 > 10
# False : 0, 0.0, (), [], {} ''(빈 문자열), None인 경우
# True : False인 경우를 제외한 값이 할당된 경우


print("None >> ", bool(None))  # None

print("불린 True >> ", bool(True))  # 불린 타입

print("불린 False >> ", bool(False))  # 불린 타입

print("숫자 13 >> ", bool(13))  # 숫자 계열

print("숫자 0.0) >> ", bool(0.0))  # 숫자 계열

print("빈 문자열 >> ", bool(""))  # 문자열

print("'apple' 문자열 >> ", bool("apple"))  # 문자열

print("빈 튜플 () >> ", bool(()))  # 튜플

print("빈 리스트 [] >> ", bool([]))  # 리스트

print("[10, 'Apple']) >> ", bool([10, "Apple"]))  # 리스트

print("빈 딕셔너리 {} >> ", bool({}))  # 딕셔너리

print("{'a': 1} >> ", bool({"a": 1}))  # 딕셔너리
