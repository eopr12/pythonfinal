@echo off
color 17
setlocal enableDelayedExpansion

rem bat 파일을 실행할 때는 파일 저장 형식이 중요합니다.
rem bat 파일을 utf-8 방식으로 저장하면 실행이 안될 수도 있음.
rem bat 파일을 저장할 때는 반드시 ASCII 방식으로 저장해야 한다.
rem
rem bat 파일을 사용하여 파이썬 소스를 실행한다.
rem bat 파일 작성법은 https://jangpd007.tistory.com/163 을 참조하세요.
rem
rem bat 파일을 윈도우 서비스로 등록하는 방법은 구글 검색한다.
rem https://potensj.tistory.com/108
rem

rem @@@@@@@@@@@@@@@@@@@@@
rem step 2. 현재 디렉토리 확인
rem @@@@@@@@@@@@@@@@@@@@@
SET CURRENTDIR=%CD%
echo %CURRENTDIR%

rem 빈줄 추가
echo.

rem %PYTHONPATH%\python.exe %CURRENTDIR%\py소스.py

python.exe %CURRENTDIR%\배치.py


PAUSE
EXIT


