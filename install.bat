@echo off
chcp 936 >nul
title 说英语 - 安装环境
cd /d "%~dp0"

echo ============================================
echo   说英语 - 首次安装（大约需要 2-5 分钟）
echo ============================================
echo.

set "PY=python"
where py >nul 2>nul
if not errorlevel 1 set "PY=py -3"

echo [1/3] 检查 Python ...
%PY% --version >nul 2>nul
if errorlevel 1 (
    echo.
    echo [错误] 没有找到 Python。
    echo 请先安装 Python 3.10 或更高版本：https://www.python.org/downloads/
    echo 安装时记得勾选 "Add Python to PATH"。
    echo.
    pause
    exit /b 1
)
%PY% --version

echo.
echo [2/3] 创建项目专用运行环境 .venv ...
if not exist ".venv\Scripts\python.exe" (
    %PY% -m venv --system-site-packages .venv
    if errorlevel 1 (
        echo [错误] 创建虚拟环境失败。
        pause
        exit /b 1
    )
) else (
    echo 已存在，跳过。
)

echo.
echo [3/3] 安装依赖（语音识别等）...
".venv\Scripts\python.exe" -m pip install --upgrade pip --quiet
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo [错误] 依赖安装失败，请检查网络后重试。
    pause
    exit /b 1
)

echo.
echo ============================================
echo   安装完成！现在可以双击 start.bat 开始学习。
echo ============================================
echo.
pause
