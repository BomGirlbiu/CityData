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
) else (
    REM ɾ��./province_city_dict.json�ļ�
    if exist ./province_city_dict.json (
        del ./province_city_dict.json
        if %errorlevel% neq 0 (
            echo ɾ��./province_city_dict.jsonʧ��
            exit /b %errorlevel%
        )
    )
)

REM �������⻷��
call %VENV_PATH%\Scripts\activate

REM ִ��Get_city_news_url.py ./city_dict.json
python Get_city_news_url.py ./province_city_dict.json
if %errorlevel% neq 0 (
    echo Get_city_news_url.py ִ��ʧ��
    exit /b %errorlevel%
)

REM ִ��Combine_city_news.py
python Combine_city_news_url.py
if %errorlevel% neq 0 (
    echo Combine_city_news.py ִ��ʧ��
    exit /b %errorlevel%
)

REM ִ��ƴ��ת����.py
python ƴ��ת����.py
if %errorlevel% neq 0 (
    echo ƴ��ת����.py ִ��ʧ��
    exit /b %errorlevel%
)

python save_to_db.py
if %errorlevel% neq 0 (
    echo save_to_db.py ִ��ʧ��
    exit /b %errorlevel%
)

echo ���нű�ִ�гɹ�
endlocal