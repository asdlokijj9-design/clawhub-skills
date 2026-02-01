@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo 🦞 开始 ClawHub Skills 同步...
echo.

echo 📊 步骤1/3: 运行 sync_full.py
python sync_full.py
if %errorlevel% neq 0 (
    echo ❌ sync_full.py 执行失败
    exit /b 1
)
echo.

echo 📄 步骤2/3: 运行 generate_feishu.py
python generate_feishu.py
if %errorlevel% neq 0 (
    echo ❌ generate_feishu.py 执行失败
    exit /b 1
)
echo.

echo 📋 步骤3/3: 生成 feishu_complete.md (完整版)
echo 完整版已就绪，详情见 feishu_complete.md
echo.

echo ✅ ClawHub Skills 同步完成！
echo.
pause
