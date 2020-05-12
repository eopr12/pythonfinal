
# 오류의 종류에 따라서 서로 다른 예외 처리가 가능하다


try:
    # 딕셔너리를 선언합니다.
    dictionary = {
        "name": "7D 건조 망고",
        "type": "당절임",
        "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
        "origin": "필리핀"
    }

    # 존재하지 않는 키에 접근해봅니다.
    dictionary["존재하지 않는 키"]
except Exception as ex:
    print("Exception",  ex)  # 로그 파일에 저장하는 방식으로 수정 필요
