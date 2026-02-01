# -*- coding: utf-8 -*-
"""测试后台任务管理器"""
import sys
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from task_manager import tm

print("🚀 测试后台任务功能\n")

# 启动3个后台任务
print("1. 启动后台任务...")
result1 = tm.run_background("python -c \"import time; time.sleep(3); print('任务1完成')\"", "测试任务1")
print(result1)

print("2. 启动后台任务...")
result2 = tm.run_background("python -c \"import time; time.sleep(2); print('任务2完成')\"", "测试任务2")
print(result2)

print("3. 启动后台任务...")
result3 = tm.run_background("dir", "列出目录")
print(result3)

print("\n📋 查看任务列表:")
print(tm.list_tasks())

print("\n✅ 测试完成！任务正在后台运行，你可以继续和助手对话")
