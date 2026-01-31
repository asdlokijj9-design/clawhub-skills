# -*- coding: utf-8 -*-
"""
ClawHub Skills 同步 - 精细分类版
根据具体功能和名称进行分类
"""

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
import os
import subprocess
from datetime import datetime

SKILLS_DIR = r"D:\moltbot开发项目\06_待优化方案\clawhub_skills"
DB_FILE = os.path.join(SKILLS_DIR, "skills_db.json")
README_FILE = os.path.join(SKILLS_DIR, "README.md")
GITHUB_REPO = "https://github.com/asdlokijj9-design/clawhub-skills"

# 分类映射（中文显示名称）
CATEGORIES = {
    "voice-activation": "语音交互",
    "text-to-speech": "语音合成",
    "image-analysis": "图像AI",
    "web-search": "网络搜索",
    "web-fetch": "网页抓取",
    "browser-control": "浏览器控制",
    "memory-management": "记忆管理",
    "file-operations": "文件操作",
    "shell-execution": "Shell执行",
    "bluebubbles": "消息渠道",
    "session-management": "会话管理",
    "cron-scheduler": "定时任务",
    "gateway-management": "系统管理",
    "canvas-control": "画布控制",
    "node-control": "节点控制",
    "skill-creator": "开发工具",
    "feishu-doc": "飞书文档",
    "feishu-app": "飞书权限",
    "feishu-folder": "飞书文件夹",
}

# 二级分类分组
GROUPS = {
    "语音交互": ["voice-activation", "text-to-speech"],
    "信息获取": ["web-search", "web-fetch"],
    "AI分析": ["image-analysis"],
    "浏览器自动化": ["browser-control"],
    "知识管理": ["memory-management"],
    "文件系统": ["file-operations", "shell-execution"],
    "消息通信": ["bluebubbles", "session-management"],
    "系统运维": ["cron-scheduler", "gateway-management", "canvas-control", "node-control"],
    "开发工具": ["skill-creator"],
    "飞书集成": ["feishu-doc", "feishu-app", "feishu-folder"],
}

# 完整 Skills 列表
ALL_SKILLS = [
    {"name": "voice-activation", "displayName": "语音唤醒", "description": "语音唤醒词检测，支持自定义关键词", "category": "voice-activation"},
    {"name": "text-to-speech", "displayName": "文字转语音 (TTS)", "description": "将文本转换为语音并返回 MEDIA 路径", "category": "text-to-speech"},
    {"name": "image-analysis", "displayName": "图像分析", "description": "使用配置的图像模型分析图像内容", "category": "image-analysis"},
    {"name": "web-search", "displayName": "网络搜索", "description": "使用 Brave Search API 进行网络搜索", "category": "web-search"},
    {"name": "web-fetch", "displayName": "网页内容抓取", "description": "从 URL 获取并提取可读内容（HTML 转 Markdown/文本）", "category": "web-fetch"},
    {"name": "browser-control", "displayName": "浏览器控制", "description": "通过 OpenClaw 浏览器控制服务控制浏览器（导航、点击、截图等）", "category": "browser-control"},
    {"name": "memory-management", "displayName": "记忆管理", "description": "语义搜索和读取记忆文件（MEMORY.md, memory/*.md）", "category": "memory-management"},
    {"name": "file-operations", "displayName": "文件操作", "description": "读取、写入、编辑文件内容", "category": "file-operations"},
    {"name": "shell-execution", "displayName": "Shell 命令执行", "description": "执行 Shell 命令，支持 PTY、后台运行和超时控制", "category": "shell-execution"},
    {"name": "bluebubbles", "displayName": "BlueBubbles 消息", "description": "BlueBubbles 外部频道插件，支持 REST API 发送/探测和 Webhook 接收", "category": "bluebubbles"},
    {"name": "session-management", "displayName": "会话管理", "description": "列出、发送消息和获取其他会话/子代理的历史", "category": "session-management"},
    {"name": "cron-scheduler", "displayName": "定时任务调度", "description": "管理 Gateway 定时任务和唤醒事件", "category": "cron-scheduler"},
    {"name": "gateway-management", "displayName": "Gateway 管理", "description": "重启、配置或更新 Gateway 服务", "category": "gateway-management"},
    {"name": "canvas-control", "displayName": "画布控制", "description": "控制节点画布（呈现/隐藏/截图/A2UI）", "category": "canvas-control"},
    {"name": "node-control", "displayName": "节点控制", "description": "发现和控制配对节点（状态/描述/相机/屏幕/位置/运行）", "category": "node-control"},
    {"name": "skill-creator", "displayName": "Skill 创建器", "description": "创建或更新 AgentSkills，包含脚本、引用和资源", "category": "skill-creator"},
    {"name": "feishu-doc", "displayName": "飞书文档", "description": "飞书文档操作（创建/读取/写入/更新/删除/追加）", "category": "feishu-doc"},
    {"name": "feishu-app", "displayName": "飞书应用", "description": "列出当前飞书应用权限（Scopes），用于调试权限问题", "category": "feishu-app"},
    {"name": "feishu-folder", "displayName": "飞书文件夹", "description": "列出飞书文件夹中的文档和子文件夹", "category": "feishu-folder"},
]

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"skills": [], "last_sync": None}

def save_db(db):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def main():
    print("=" * 60)
    print("  ClawHub Skills 同步 - 精细分类版")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()
    
    db = load_db()
    before = len(db["skills"])
    
    # 添加所有 Skills 到数据库
    for skill_data in ALL_SKILLS:
        # 检查是否已存在
        exists = False
        for existing in db["skills"]:
            if existing.get("category") == skill_data["category"]:
                exists = True
                break
        
        if not exists:
            skill = {
                "name": skill_data["name"],
                "displayName": skill_data["displayName"],
                "url": f"https://www.clawhub.ai/skills/{skill_data['name']}",
                "description": skill_data["description"],
                "category": skill_data["category"],
                "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            db["skills"].append(skill)
    
    db["last_sync"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_db(db)
    
    print(f"数据库: {len(db['skills'])} Skills")
    print()
    
    # 生成 README
    readme = f"""# ClawHub Skills 同步仓库

**最后同步:** {db['last_sync']}  
**GitHub:** [View]({GITHUB_REPO})  
**官网:** [ClawHub](https://www.clawhub.ai/skills)

---

## 统计概览

| 分类 | 数量 |
|------|------|
"""
    
    for group, cats in GROUPS.items():
        count = len([s for s in db["skills"] if s["category"] in cats])
        readme += f"| {group} | {count} |\n"
    
    total = len(db["skills"])
    readme += f"| **总计** | **{total}** |\n"
    
    readme += "\n---\n\n## 分类详情\n\n"
    
    for group, cats in GROUPS.items():
        readme += f"### {group}\n\n"
        
        for cat in cats:
            skill = next((s for s in db["skills"] if s["category"] == cat), None)
            if skill:
                displayName = skill.get("displayName", skill["name"])
                desc = skill.get("description", "")
                url = skill.get("url", "")
                readme += f"#### {displayName}\n\n"
                readme += f"- **描述:** {desc}\n"
                readme += f"- **链接:** [{url}]({url})\n"
                readme += f"- **分类:** {skill['category']}\n"
                readme += "\n"
    
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(readme)
    
    print("README.md 已更新")
    print()
    
    # Git 提交推送
    print("Git 同步...")
    subprocess.run(["git", "add", "-A"], cwd=SKILLS_DIR, capture_output=True)
    subprocess.run(["git", "commit", "-m", f"Refine: {len(db['skills'])} skills with detailed categories"], cwd=SKILLS_DIR, capture_output=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=SKILLS_DIR, capture_output=True, timeout=30)
    print("已推送到 GitHub")
    print()
    
    print("=" * 60)
    print(f"  完成! {len(db['skills'])} Skills")
    print("=" * 60)

if __name__ == '__main__':
    main()
