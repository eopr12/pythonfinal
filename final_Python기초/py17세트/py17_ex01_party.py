# 파티에 참석한 사람들의 명단이 세트 A와 B에 각각 저장되어 있다. 
# 2개 파티에 모두 참석한 사람들의 명단을 출력하려면 어떻게 해야 할까? 
# 2개의 파티에 모두 참석한 사람은 다음과 같습니다. 
# {'Park'}


partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])

print("2개의 파티에 모두 참석한 사람은 다음과 같습니다. ")
print ( partyA.intersection(partyB))
