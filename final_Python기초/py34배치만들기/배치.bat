@echo off
color 17
setlocal enableDelayedExpansion

rem bat ������ ������ ���� ���� ���� ������ �߿��մϴ�.
rem bat ������ utf-8 ������� �����ϸ� ������ �ȵ� ���� ����.
rem bat ������ ������ ���� �ݵ�� ASCII ������� �����ؾ� �Ѵ�.
rem
rem bat ������ ����Ͽ� ���̽� �ҽ��� �����Ѵ�.
rem bat ���� �ۼ����� https://jangpd007.tistory.com/163 �� �����ϼ���.
rem
rem bat ������ ������ ���񽺷� ����ϴ� ����� ���� �˻��Ѵ�.
rem https://potensj.tistory.com/108
rem

rem @@@@@@@@@@@@@@@@@@@@@
rem step 2. ���� ���丮 Ȯ��
rem @@@@@@@@@@@@@@@@@@@@@
SET CURRENTDIR=%CD%
echo %CURRENTDIR%

rem ���� �߰�
echo.

rem %PYTHONPATH%\python.exe %CURRENTDIR%\py�ҽ�.py

python.exe %CURRENTDIR%\��ġ.py


PAUSE
EXIT


