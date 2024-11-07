@echo off
setlocal

REM 接受Python虚拟环境地址作为第一个参数
set VENV_PATH=%1

REM 激活虚拟环境
call %VENV_PATH%\Scripts\activate

REM 执行Get_city_news_url.py ./city_dict.json
python Get_city_news_url.py ./province_city_dict.json
if %errorlevel% neq 0 (
    echo Get_city_news_url.py 执行失败
    exit /b %errorlevel%
)

REM 执行Combine_city_news.py
python Combine_city_news_url.py
if %errorlevel% neq 0 (
    echo Combine_city_news.py 执行失败
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