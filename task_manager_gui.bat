@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo 🎯 OpenClaw 后台任务管理器
echo =============================
echo.
echo 命令:
echo   1. 任务列表     - 查看所有后台任务
echo   2. 状态 [ID]    - 查看任务详细状态
echo   3. 输出 [ID]    - 获取任务输出
echo   4. 终止 [ID]    - 终止任务
echo   5. 清理         - 清理已完成任务
echo   6. 测试         - 运行测试任务
echo   7. 退出
echo.

:menu
set /p choice="请输入命令编号: "

if "%choice%"=="1" (
    python -c "from task_manager import tm; print(tm.list_tasks())"
    goto menu
)

if "%choice%"=="2" (
    set /p tid="请输入任务ID: "
    python -c "from task_manager import tm; print(tm.tasks.get('%tid%', {'status': '未知'}))"
    goto menu
)

if "%choice%"=="3" (
    set /p tid="请输入任务ID: "
    python -c "from task_manager import tm; print(tm.get_output('%tid%'))"
    goto menu
)

if "%choice%"=="4" (
    set /p tid="请输入任务ID: "
    python -c "from task_manager import tm; print(tm.kill_task('%tid%'))"
    goto menu
)

if "%choice%"=="5" (
    python -c "from task_manager import tm; print(tm.clear_completed())"
    goto menu
)

if "%choice%"=="6" (
    echo 运行测试任务...
    python -c "from task_manager import tm; print(tm.run_background('python -c \"import time; print(测试任务完成)\"', '测试任务'))"
    goto menu
)

if "%choice%"=="7" (
    echo 再见！
    exit /b 0
)

echo 无效命令
goto menu
