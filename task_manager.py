# -*- coding: utf-8 -*-
"""
OpenClaw 后台任务管理器
支持：后台执行、状态查询、结果获取、任务取消
"""

import subprocess
import threading
import queue
import os
import json
from datetime import datetime
from pathlib import Path

TASK_DIR = Path("~/.openclaw/workspace/task_manager").expanduser()
TASK_DIR.mkdir(parents=True, exist_ok=True)

class TaskManager:
    """后台任务管理器"""
    
    def __init__(self):
        self.tasks = {}
        self.log_file = TASK_DIR / "tasks.log"
    
    def run_background(self, command: str, name: str = None) -> str:
        """
        启动后台任务
        用法:
        - tm.run_background("python sync.py", "同步数据")
        - tm.run_background("git push", "推送代码")
        """
        import uuid
        task_id = str(uuid.uuid4())[:8]
        name = name or command[:30]
        
        # 启动进程
        proc = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        self.tasks[task_id] = {
            "id": task_id,
            "name": name,
            "command": command,
            "process": proc,
            "status": "running",
            "start_time": datetime.now().isoformat(),
            "output": ""
        }
        
        # 异步读取输出
        def read_output(proc, task_id):
            stdout, stderr = proc.communicate()
            self.tasks[task_id]["output"] = stdout + stderr
            self.tasks[task_id]["status"] = "completed" if proc.returncode == 0 else "failed"
            self.tasks[task_id]["end_time"] = datetime.now().isoformat()
        
        threading.Thread(target=read_output, args=(proc, task_id), daemon=True).start()
        
        return f"""
🎯 **后台任务已启动**
- ID: `{task_id}`
- 名称: {name}
- 命令: `{command}`
- 状态: 🏃 运行中

回复 `任务状态` 或 `查看任务` 获取最新状态
"""
    
    def list_tasks(self) -> str:
        """列出所有任务"""
        if not self.tasks:
            return "📭 没有运行中的任务"
        
        msg = "📋 **任务列表**\n\n"
        for tid, task in self.tasks.items():
            status_emoji = "🏃" if task["status"] == "running" else "✅" if task["status"] == "completed" else "❌"
            msg += f"{status_emoji} `{tid}` - {task['name']}\n"
            msg += f"   状态: {task['status']}\n"
            if "output" in task and task["output"]:
                msg += f"   输出: {task['output'][:100]}...\n"
            msg += "\n"
        return msg
    
    def get_output(self, task_id: str) -> str:
        """获取任务输出"""
        task = self.tasks.get(task_id)
        if not task:
            return f"❌ 任务 `{task_id}` 不存在"
        
        output = task.get("output", "（暂无输出）")
        return f"""
📄 任务 `{task['name']}` 输出:
```
{output}
```
"""
    
    def kill_task(self, task_id: str) -> str:
        """终止任务"""
        task = self.tasks.get(task_id)
        if not task:
            return f"❌ 任务 `{task_id}` 不存在"
        
        task["process"].terminate()
        task["status"] = "killed"
        return f"🛑 任务 `{task_id}` 已终止"
    
    def clear_completed(self) -> str:
        """清理已完成的任务"""
        completed = [tid for tid, t in self.tasks.items() if t["status"] != "running"]
        for tid in completed:
            del self.tasks[tid]
        return f"🧹 已清理 {len(completed)} 个完成的任务"

# 全局实例
tm = TaskManager()

# 便捷函数
def 后台运行(命令: str, 名称: str = None) -> str:
    """启动后台任务"""
    return tm.run_background(命令, 名称)

def 任务列表() -> str:
    """查看所有任务"""
    return tm.list_tasks()

def 任务输出(任务ID: str) -> str:
    """获取任务输出"""
    return tm.get_output(任务ID)

def 终止任务(任务ID: str) -> str:
    """终止任务"""
    return tm.kill_task(任务ID)

def 清理任务() -> str:
    """清理已完成任务"""
    return tm.clear_completed()

if __name__ == "__main__":
    # 测试
    print("TaskManager 已加载")
    print("可用函数: 后台运行(), 任务列表(), 任务输出(), 终止任务(), 清理任务()")
