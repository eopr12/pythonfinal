
# 패키지의 모듈을 사용해보겠습니다. 
#
# import 패키지.모듈
# 패키지.모듈.변수
# 패키지.모듈.함수()
# 패키지.모듈.클래스()


# mylib.graphic 패키지의 geometry 모듈을 import
import mylib.graphic.geometry
import mylib.graphic.test

# mylib.sound 패키지의 echo 모듈을 import
import mylib.sound.echo 

# mylib.operation 패키지의 run 모듈을 import
import mylib.operation.run

# mylib.graphic 패키지 geometry 모듈의 triangle_area 함수 사용
value = mylib.graphic.geometry.triangle_area(30,40)
print(value)

# mylib.graphic 패키지 geometry 모듈의 rectangle_area 함수 사용
value = mylib.graphic.geometry.rectangle_area(30,40)
print(value)

# mylib.graphic 패키지 test 모듈의 test_graphic 함수 사용
value = mylib.graphic.test.test_graphic()
print(value)

# mylib.operation 패키지 run 모듈의 render_test 함수 사용
print(mylib.operation.run.render_test())
