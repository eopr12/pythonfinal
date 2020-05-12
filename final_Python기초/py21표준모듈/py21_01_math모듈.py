##########################
# import 방법 3가지
# import 구문 : import math
# from 구문   : from math import sin, cos, tan, floor, ceil
# as 구문     : import math as m
#
#               import math
#               mt = math
#########################

# 모듈을 읽어 들입니다.
from math import sin, cos, tan, floor, ceil
import math as m
import math


#################################
# math 모듈의 사용법을 익힌다.
#
# math.sin()
# math.cos()
# math.tan()
# math.floor()
# math.ceil()
# math.round()
#################################

# sin, cos, tan, 내림과 올림을 구합니다.
print( "math.sin(1)     = ", math.sin(1)     )
print( "math.cos(1)     = ", math.cos(1)     )
print( "math.tan(1)     = ", math.tan(1)     )
print( "math.floor(2.5) = ", math.floor(2.5) )
print( "math.ceil(2.5)  = ", math.ceil(2.5)  )

# sin, cos, tan, 내림과 올림을 구합니다.
mh = math # math 의 nickname 설정.
print("mh.sin(1):", mh.sin(1))
print("mh.cos(1):", mh.cos(1))
print("mh.tan(1):", mh.tan(1))
print("mh.floor(2.5):", mh.floor(2.5))
print("mh.ceil(2.5):", mh.ceil(2.5))



# sin, cos, tan, 내림과 올림을 구합니다.
print("m.sin(1):", m.sin(1))
print("m.cos(1):", m.cos(1))
print("m.tan(1):", m.tan(1))
print("m.floor(2.5):", m.floor(2.5))
print("m.ceil(2.5):", m.ceil(2.5))


# sin, cos, tan, 내림과 올림을 구합니다.
print("sin(1):", sin(1))
print("cos(1):", cos(1))
print("tan(1):", tan(1))
print("floor(2.5):", floor(2.5))
print("ceil(2.5):", ceil(2.5))

print("홀수 round(1.5):", round(1.5))
print("짝수 round(2.5):", round(2.5))
print("홀수 round(3.5):", round(3.5))
print("짝수 round(4.5):", round(4.5))
