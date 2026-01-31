@echo off
chcp 65001 >nul
echo.
echo ========================================
echo    ClawHub Skills 同步
echo ========================================
echo.

cd /d "D:\moltbot开发项目\06_待优化方案\clawhub_skills"

python sync.py

echo.
pause
