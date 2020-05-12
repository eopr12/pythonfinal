####################
# import 방식
# 	import 모듈명
#   import 모듈명 as 별칭
# 	from 모듈명 import 함수명
####################


####################
# import 모듈명
import mod

####################
# import 모듈명 as 별칭
import mod as 별칭

####################
# from 모듈명 import 함수명
from mod import sum


print("import 모듈명             >> mod.add(3, 4)  = ", mod.add(3, 4))  # 7
print("import 모듈명 as 별칭     >> 별칭.add(3, 4) = ", 별칭.add(3, 4))  # 7
print("from 모듈명 import 함수명 >> sum(3, 4)      = ", sum(3, 4))  # 7
