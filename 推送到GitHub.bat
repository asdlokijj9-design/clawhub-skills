@echo off
chcp 65001 >nul
echo.
echo ========================================
echo    🚀 一键推送到 GitHub
echo ========================================
echo.
echo  步骤：
echo  1. 打开 https://github.com/new
echo  2. 创建名为 'clawhub-skills' 的仓库
echo  3. 不要勾选任何选项（README, .gitignore 等）
echo  4. 点击 'Create repository'
echo  5. 复制仓库地址（HTTPS 格式）
echo  6. 粘贴到下方
echo.
echo ========================================

cd /d "%~dp0"

echo.
set /p repo_url="请粘贴仓库地址 (例如: https://github.com/用户名/clawhub-skills): "

if "%repo_url%"=="" (
    echo ❌ 未输入仓库地址
    pause
    exit /b 1
)

echo.
echo 🔗 添加远程仓库...
git remote add origin "%repo_url%"

echo.
echo 🚀 推送到 GitHub...
git push -u origin master

echo.
echo ========================================
echo  ✅ 推送完成！
echo ========================================
echo.
pause
