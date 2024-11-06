@echo off
setlocal

REM 接受Python虚拟环境地址作为第一个参数
set VENV_PATH=%1

REM 激活虚拟环境
call %VENV_PATH%\Scripts\activate

REM 执行Get_city_scenic_spots.py
python Get_city_scenic_spots.py
if %errorlevel% neq 0 (
    echo Get_city_scenic_spots.py 执行失败
    exit /b %errorlevel%
)

echo 脚本执行成功
endlocal