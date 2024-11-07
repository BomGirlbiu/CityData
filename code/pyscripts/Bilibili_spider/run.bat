@echo off
setlocal enabledelayedexpansion

REM 解析命令行参数
set "venv_path="

:parse_args
if "%~1"=="" goto :end_parse_args
if "%~1"=="-v" (
    set "venv_path=%~2"
    shift
    shift
    goto :parse_args
)
shift
goto :parse_args

:end_parse_args

if "%venv_path%"=="" (
    echo 请输入虚拟环境地址作为参数
    exit /b 1
)

REM 激活虚拟环境
call %venv_path%\Scripts\activate

REM 定义脚本列表
set scripts[1]=Get_videos_links.py ./province_city_dict.json
set scripts[2]=combind.py
set scripts[3]=Get_comments.py
set scripts[4]=combind.py 1
set scripts[5]=Sentiment_analysis.py
set scripts[6]=save_comments.py

REM 运行每个脚本
for /L %%i in (1,1,6) do (
    python !scripts[%%i]!
    if errorlevel 1 (
        echo !scripts[%%i]! 执行失败。
        exit /b 1
    )
)

REM 关闭虚拟环境
deactivate
endlocal