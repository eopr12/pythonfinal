#####################
# 얕은 복사 vs 깊은 복사
#####################
scores = [10, 20, 30, 40, 50]
print("scores 리스트", scores)
print("scores address", id(scores))

#####################
# 리스트 복사
#####################
values1 = scores  # 리스트 복사
print("values1 리스트", values1)
print("values1 address", id(values1))

#####################
# 리스트 복제
#####################
values2 = list(scores)  # 리스트 복제
print("values2 리스트", values2)
print("values2 address", id(values2))
