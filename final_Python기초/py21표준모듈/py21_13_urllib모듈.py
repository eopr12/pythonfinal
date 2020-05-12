
#################################
# urllib 모듈의 사용법을 익힌다.
#
# urllib는 파이썬에서 웹과 관련된 데이터를 손쉽게 이용하도록 도와주는 라이브러리입니다
#
# urllib.request.urlopen()	웹에서 얻은 데이터에 대한 객체를 반환해줍니다.
# urllib.request.read()	웹에서 얻은 데이터에 대한 객체를 반환해줍니다.
#################################

# 웹 문서를 불러오기
# 웹 페이지의 데이터를 읽어오기
# 웹 서버 정보 받아오기
# 웹 페이지의 상태 확인하기


# 모듈을 읽어 들입니다.
import urllib.request as req
from urllib import request

# import urllib.request
# req = urllib.request


# 웹 문서를 불러오
# urlopen 함수의 인자는 데이터를 얻고 싶은 웹 페이지의 주소를 주면 됩니다.
# urlopen 함수는 웹에서 얻은 데이터에 대한 객체를 반환해줍니다.
# 실행 예시)
# <http.client.HTTPResponse object at 0x000001C784AE2240>
res = req.urlopen("https://www.naver.com")
print(res)



# 웹 서버 정보 받아오기
# getheaders() 함수를 사용하면 서버에 대한 정보를 리스트로 돌려줍니다.
# 출력된 결과를 통해 운영체제나 날짜, 타입 등 여러 가지 정보를 알 수 있으며
# 이 정보들은 크롤링하려는 홈페이지가 어떤 형식으로 만들어 졌는지 알 수 있습니다.
# 실행 예시)
# ('Server', 'NWS')
# ('Date', 'Tue, 22 May 2018 06:35:45 GMT')
# ('Content-Type', 'text/html; charset=UTF-8')
# ('Transfer-Encoding', 'chunked')
# ('Connection', 'close')
# ('Cache-Control', 'no-cache, no-store, must-revalidate')
# ('Pragma', 'no-cache')
# ('P3P', 'CP="CAO DSP CURa ADMa TAIa PSAa OUR LAW STP PHY ONL UNI PUR FIN COM NAV INT DEM STA PRE"')
# ('X-Frame-Options', 'SAMEORIGIN')
# ('Strict-Transport-Security', 'max-age=31536000; preload')
# ('Referrer-Policy', 'unsafe-url')
d = req.urlopen("https://www.naver.com")
status = d.getheaders()
for i in status:
    print(i)



# 웹 페이지의 상태 확인하기
d = req.urlopen("https://www.naver.com")
print( d.status ) # 200



# 웹 페이지의 데이터를 읽어오기#
# read() 함수를 사용하게 되면 문서의 HTML 코드를 출력합니다. 크롤러를 제작할 때도
# read() 함수를 사용해서 HTML 코드를 불러온 뒤 원하는 데이터만 골라내는 작업을 하게 됩니다.
# 실행 예시)
# b'<html>\n<head>\n<title>The Python Challenge</title>\n<meta name="keywords"\n content="Python Challenge, Python, Challenge, programming language, learning python, exploring python, riddle, mylib, puzzle, brain teasers" />\n <meta name ="description" content="Python Challenge home page,\nThe ....... 이하 생략#
d = req.urlopen('http://www.pythonchallenge.com/')
print( d.read() )




# urlopen() 함수로 구글의 메인 페이지 읽기
target = request.urlopen("https://google.com")
output = target.read()
print(output)

# write binary[바이너리 쓰기] 모드로
file = open("output.html", "w")
file.write(output)


# urlopen() 함수로 이미지 읽기
target = request.urlopen(
    "http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

# write binary[바이너리 쓰기] 모드로
file = open("output.png", "wb")
file.write(output)
