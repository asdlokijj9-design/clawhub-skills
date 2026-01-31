# -*- coding: utf-8 -*-
"""
同步已知的 ClawHub Skills 到数据库
"""

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
import os
from datetime import datetime

SKILLS_DIR = r"D:\moltbot开发项目\06_待优化方案\clawhub_skills"
DB_FILE = os.path.join(SKILLS_DIR, "skills_db.json")
README_FILE = os.path.join(SKILLS_DIR, "README.md")
GITHUB_REPO = "https://github.com/asdlokijj9-design/clawhub-skills"

CATEGORY_MAP = {
    "voice": "Voice - 语音相关",
    "browser": "Browser - 浏览器相关",
    "memory": "Memory - 记忆相关",
    "message": "Message - 消息相关",
    "file": "File - 文件相关",
    "developer": "Developer - 开发相关",
    "image": "Image - 图片相关",
    "calendar": "Calendar - 日程相关",
    "ecommerce": "Ecommerce - 电商相关",
    "ai": "AI - 人工智能相关",
    "other": "Other - 其他"
}

# 已知的 Skills
KNOWN_SKILLS = [
    {"name": "bluebubbles", "url": "https://www.clawhub.ai/skills/bluebubbles", "description": "BlueBubbles 外部频道插件，支持 REST API 发送/探测和 Webhook 接收", "category": "message"},
    {"name": "skill-creator", "url": "https://www.clawhub.ai/skills/skill-creator", "description": "创建或更新 AgentSkills，包含脚本、引用和资源", "category": "developer"},
    {"name": "voice-activation", "url": "https://www.clawhub.ai/skills/voice-activation", "description": "语音唤醒词检测，支持自定义关键词", "category": "voice"},
    {"name": "web-search", "url": "https://www.clawhub.ai/skills/web-search", "description": "使用 Brave Search API 进行网络搜索", "category": "browser"},
    {"name": "web-fetch", "url": "https://www.clawhub.ai/skills/web-fetch", "description": "从 URL 获取并提取可读内容（HTML 转 Markdown/文本）", "category": "browser"},
    {"name": "browser-control", "url": "https://www.clawhub.ai/skills/browser-control", "description": "通过 OpenClaw 浏览器控制服务控制浏览器", "category": "browser"},
    {"name": "memory-management", "url": "https://www.clawhub.ai/skills/memory-management", "description": "语义搜索和读取记忆文件（MEMORY.md, memory/*.md）", "category": "memory"},
    {"name": "session-management", "url": "https://www.clawhub.ai/skills/session-management", "description": "列出、发送消息和获取其他会话/子代理的历史", "category": "message"},
    {"name": "file-operations", "url": "https://www.clawhub.ai/skills/file-operations", "description": "读取、写入、编辑文件内容", "category": "file"},
    {"name": "shell-execution", "url": "https://www.clawhub.ai/skills/shell-execution", "description": "执行 Shell 命令，支持 PTY、后台运行和超时控制", "category": "developer"},
    {"name": "text-to-speech", "url": "https://www.clawhub.ai/skills/text-to-speech", "description": "将文本转换为语音并返回 MEDIA 路径", "category": "voice"},
    {"name": "image-analysis", "url": "https://www.clawhub.ai/skills/image-analysis", "description": "使用配置的图像模型分析图像", "category": "image"},
    {"name": "cron-scheduler", "url": "https://www.clawhub.ai/skills/cron-scheduler", "description": "管理 Gateway 定时任务和唤醒事件", "category": "calendar"},
    {"name": "gateway-management", "url": "https://www.clawhub.ai/skills/gateway-management", "description": "重启、配置或更新 Gateway 服务", "category": "developer"},
    {"name": "canvas-control", "url": "https://www.clawhub.ai/skills/canvas-control", "description": "控制节点画布（呈现/隐藏/截图）", "category": "developer"},
    {"name": "node-control", "url": "https://www.clawhub.ai/skills/node-control", "description": "发现和控制配对节点（状态/描述/相机/屏幕/位置/运行）", "category": "developer"},
    {"name": "feishu-doc", "url": "https://www.clawhub.ai/skills/feishu-doc", "description": "飞书文档操作（创建/读取/写入/更新/删除/追加）", "category": "message"},
    {"name": "feishu-app", "url": "https://www.clawhub.ai/skills/feishu-app", "description": "列出当前飞书应用权限（Scopes）", "category": "message"},
    {"name": "feishu-folder", "url": "https://www.clawhub.ai/skills/feishu-folder", "description": "列出飞书文件夹中的文档和子文件夹", "category": "file"},
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
    print("  同步已知的 ClawHub Skills")
    print("=" * 60)
    print()
    
    db = load_db()
    before = len(db["skills"])
    added = []
    
    for skill_data in KNOWN_SKILLS:
        # 检查是否已存在
        exists = False
        for existing in db["skills"]:
            if existing.get("url") == skill_data["url"]:
                exists = True
                break
        
        if not exists:
            skill = {
                "name": skill_data["name"],
                "url": skill_data["url"],
                "description": skill_data["description"],
                "category": skill_data["category"],
                "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            db["skills"].append(skill)
            added.append(skill)
            print(f"  + {skill['name']} ({skill['category']})")
    
    db["last_sync"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_db(db)
    
    print()
    print(f"  数据库: {len(db['skills'])} total, {len(added)} new")
    
    # 生成 README
    stats = {}
    for skill in db["skills"]:
        cat = skill.get("category", "other")
        stats[cat] = stats.get(cat, 0) + 1
    
    readme = f"""# ClawHub Skills 同步仓库

**最后同步:** {db['last_sync']}  
**GitHub:** [View]({GITHUB_REPO})  
**官网:** [ClawHub](https://www.clawhub.ai/skills)

---

## 统计概览

| 分类 | 数量 |
|------|------|
"""
    total = 0
    for cat in sorted(stats.keys()):
        cat_name = CATEGORY_MAP.get(cat, cat)
        count = stats[cat]
        total += count
        readme += f"| {cat_name} | {count} |\n"
    readme += f"| **总计** | **{total}** |\n"
    readme += "\n---\n\n## 分类详情\n\n"
    for cat in sorted(stats.keys()):
        cat_name = CATEGORY_MAP.get(cat, cat)
        readme += f"### {cat_name}\n\n"
        for skill in db["skills"]:
            if skill.get("category") == cat:
                name = skill.get("name", "Unknown")
                desc = skill.get("description", "")
                readme += f"- **{name}** - {desc}\n"
        readme += "\n"
    
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(readme)
    
    print(f"  README.md 已更新")
    print()
    print("=" * 60)
    
    return db, added

if __name__ == '__main__':
    main()
