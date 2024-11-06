@echo off
setlocal

if "%1"=="" (
    echo 请输入虚拟环境地址作为参数
    exit /b 1
)

REM 激活虚拟环境
call %1\Scripts\activate

REM 解析跳过脚本的参数
set skip_scripts=%2 %3 %4 %5 %6 %7 %8 %9

REM 定义脚本列表
set scripts[1]=Get_videos_links.py ./province_city_dict.json
set scripts[2]=combind.py
set scripts[3]=Get_comments.py
set scripts[4]=combind.py 1
set scripts[5]=Sentiment_analysis.py
set scripts[6]=save_comments.py

REM 运行每个脚本并检查是否需要跳过
setlocal enabledelayedexpansion
for /L %%i in (1,1,6) do (
    set skip=0
    for %%j in (%skip_scripts%) do (
        if "%%j"=="%%i" (
            set skip=1
        )
    )
    if !skip! equ 0 (
        python !scripts[%%i]!
        if errorlevel 1 (
            echo !scripts[%%i]! 执行失败。
            exit /b 1
        )
    )
)

REM 关闭虚拟环境
deactivate
endlocal