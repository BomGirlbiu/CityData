@echo off
setlocal

set VENV_PATH=%1

REM 激活虚拟环境
call %VENV_PATH%\Scripts\activate

REM 执行 Get_videos_links.py
python Get_videos_links.py
if errorlevel 1 (
    echo Get_videos_links.py 执行失败。
    exit /b 1
)

REM 执行 Get_comments.py
python Get_comments.py
if errorlevel 1 (
    echo Get_comments.py 执行失败。
    exit /b 1
)

REM 执行 Sentiment_analysis.py
python Sentiment_analysis.py
if errorlevel 1 (
    echo Sentiment_analysis.py 执行失败。
    exit /b 1
)

python merge_comments.py
if errorlevel 1 (
    echo merge_comments.py 执行失败。
    exit /b 1
)

python save_comments.py
if errorlevel 1 (
    echo save_comments.py 执行失败。
    exit /b 1
)

REM 关闭虚拟环境
deactivate

echo 所有脚本执行完毕。
endlocal
exit /b 0