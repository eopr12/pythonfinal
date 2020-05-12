# import 방식
# import 모듈 : import 모듈명
#               사용방법: 모듈명.함수명
# from import : from 패키지명 import 함수명
#               사용방법: 함수명
# import as   : import 모듈명 as 별칭


# mylib.graphic 패키지의 geometry 모듈을 import
import mylib.graphic.geometry
from mylib.graphic import test

# mylib.sound 패키지의 모든 모듈을 import
from mylib.sound.echo import *

# mylib.operation 패키지의 run 모듈을 import
import mylib.operation.run as 별칭

# geometry모듈의 triangle_area(30, 40) 호출 
value = mylib.graphic.geometry.triangle_area(30, 40)
print(value)

# geometry모듈의 rectangle_area(30, 40) 호출 
value = mylib.graphic.geometry.rectangle_area(30, 40)
print(value)

# graphic 패키지 test 모듈의 test_graphic() 호출 
value = mylib.graphic.test.test_graphic()
print(value)

# 별칭 함수 호출.
value = 별칭.render_test()
print(value)
