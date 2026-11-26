@echo off
chcp 936 >nul
title 说英语 - 本地英语陪练
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo 还没有安装运行环境，先为你安装...
    call install.bat
    if not exist ".venv\Scripts\python.exe" exit /b 1
)

echo ============================================
echo   正在启动，浏览器会自动打开...
echo   关闭这个窗口就停止软件。
echo ============================================
echo.

rem 检查 Ollama 是否在运行
curl -s -o nul --max-time 2 http://127.0.0.1:11434/api/tags >nul 2>nul
if errorlevel 1 (
    echo [提示] 没检测到 Ollama 在运行。
    echo        请先启动 Ollama（开始菜单里找），否则对话功能会用不了。
    echo        不过你仍然可以先用背单词和精读功能。
    echo.
)

".venv\Scripts\python.exe" -m streamlit run streamlit_app.py --server.port 8501 --server.headless=false

echo.
echo 软件已退出。
pause
