@echo off
setlocal

REM ��������
set VENV_PATH=
set C_PARAM=

:parse_args
if "%~1"=="" goto args_done
if "%~1"=="-v" (
    set VENV_PATH=%~2
    shift
    shift
    goto parse_args
)
if "%~1"=="-c" (
    set C_PARAM=%~2
    shift
    shift
    goto parse_args
)
shift
goto parse_args

:args_done

REM ����Ƿ��ṩ��-v����
if "%VENV_PATH%"=="" (
    echo �����ṩ-v������ָ�����⻷��·��
    exit /b 1
)

REM �������⻷��
call %VENV_PATH%\Scripts\activate

REM ����ṩ��-c��������ִ��../generate_pcd.py
if not "%C_PARAM%"=="" (
    python ../generate_pcd.py %C_PARAM%
    if %errorlevel% neq 0 (
        echo ../generate_pcd.py ִ��ʧ��
        exit /b %errorlevel%
    )
)

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