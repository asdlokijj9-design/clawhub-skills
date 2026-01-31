# -*- coding: utf-8 -*-
"""
GitHub 仓库配置脚本
"""

import os
import subprocess

REPO_DIR = r"D:\moltbot开发项目\06_待优化方案\clawhub_skills"
GITHUB_EMAIL = "asdlokijj9@gmail.com"

def run_cmd(cmd, cwd=None):
    """运行命令"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def setup_github():
    print("=" * 50)
    print("  ClawHub Skills - GitHub 配置")
    print("=" * 50)
    print()
    
    # 1. 检查 Git
    print("[1/4] 检查 Git 安装...")
    ok, _, _ = run_cmd("git --version")
    if ok:
        print("  OK: Git 已安装")
    else:
        print("  Error: 请先安装 Git")
        return
    
    # 2. 配置用户
    print("\n[2/4] 配置 Git 用户...")
    run_cmd(f'git config --global user.name "Moltbot User"', cwd=REPO_DIR)
    run_cmd(f'git config --global user.email "{GITHUB_EMAIL}"', cwd=REPO_DIR)
    print("  OK: 用户已配置")
    
    # 3. 初始化仓库
    print("\n[3/4] 初始化 Git 仓库...")
    git_dir = os.path.join(REPO_DIR, ".git")
    if not os.path.exists(git_dir):
        ok, _, _ = run_cmd("git init", cwd=REPO_DIR)
        if ok:
            print("  OK: 仓库已初始化")
        else:
            print("  Error: 初始化失败")
    else:
        print("  Info: 仓库已存在")
    
    # 4. 配置 Token
    print("\n[4/4] GitHub Token 配置...")
    print()
    print("  请配置 GitHub Token（替代密码，更安全）")
    print()
    print("  步骤：")
    print("  1. 打开 https://github.com/settings/tokens")
    print("  2. 点击 'Generate new token (classic)'")
    print("  3. 设置名称：ClawHub Sync")
    print("  4. 勾选权限：repo, workflow")
    print("  5. 生成 Token")
    print()
    print("  配置方式：")
    print("  - 方式 A: 环境变量")
    print("      set GITHUB_TOKEN=ghp_xxxxx")
    print("  - 方式 B: 编辑系统环境变量")
    print()
    
    token = input("  输入 GitHub Token (直接回车跳过): ").strip()
    if token:
        os.environ["GITHUB_TOKEN"] = token
        print("  OK: Token 已临时保存")
        print("  提示：重启后失效，建议添加到系统环境变量")
    else:
        print("  Info: 跳过 Token 配置")
        print("  后续运行 sync.py 前需先配置 Token")
    
    print()
    print("=" * 50)
    print("  配置完成！")
    print("=" * 50)
    print()
    print("  下一步：")
    print("  1. 配置 GitHub Token（如未配置）")
    print("  2. 运行 sync.py 同步数据")
    print("  3. 创建 GitHub 远程仓库")
    print("  4. git remote add origin <仓库地址>")
    print("  5. git push origin main")
    print()

if __name__ == '__main__':
    setup_github()
