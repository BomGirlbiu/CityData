@echo off
setlocal

REM ����Python���⻷����ַ��Ϊ��һ������
set VENV_PATH=%1

REM �������⻷��
call %VENV_PATH%\Scripts\activate

REM ִ��Get_city_img_url.py
python Get_city_img_url.py
if %errorlevel% neq 0 (
    echo Get_city_img_url.py ִ��ʧ��
    exit /b %errorlevel%
)

REM ִ��Combine_city_img_url.py
python Combine_city_img_url.py
if %errorlevel% neq 0 (
    echo Combine_city_img_url.py ִ��ʧ��
    exit /b %errorlevel%
)

REM ִ��ƴ��ת����.py
python ƴ��ת����.py
if %errorlevel% neq 0 (
    echo ƴ��ת����.py ִ��ʧ��
    exit /b %errorlevel%
)

echo ���нű�ִ�гɹ�
endlocal