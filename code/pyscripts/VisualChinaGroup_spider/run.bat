@echo off
setlocal

REM 解析参数
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

REM 检查是否提供了-v参数
if "%VENV_PATH%"=="" (
    echo 必须提供-v参数来指定虚拟环境路径
    exit /b 1
)

REM 激活虚拟环境
call %VENV_PATH%\Scripts\activate

REM 如果提供了-c参数，先执行../generate_pcd.py
if not "%C_PARAM%"=="" (
    python ../generate_pcd.py %C_PARAM%
    if %errorlevel% neq 0 (
        echo ../generate_pcd.py 执行失败
        exit /b %errorlevel%
    )
)

REM 执行Get_city_img_url.py
python Get_city_img_url.py
if %errorlevel% neq 0 (
    echo Get_city_img_url.py 执行失败
    exit /b %errorlevel%
)

REM 执行Combine_city_img_url.py
python Combine_city_img_url.py
if %errorlevel% neq 0 (
    echo Combine_city_img_url.py 执行失败
    exit /b %errorlevel%
)

REM 执行拼音转中文.py
python 拼音转中文.py
if %errorlevel% neq 0 (
    echo 拼音转中文.py 执行失败
    exit /b %errorlevel%
)

echo 所有脚本执行成功
endlocal