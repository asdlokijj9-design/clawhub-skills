# -*- coding: utf-8 -*-
"""
生成飞书通知消息 - 精细分类版
"""

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
import os
from datetime import datetime

SKILLS_DIR = r"D:\moltbot开发项目\06_待优化方案\clawhub_skills"
DB_FILE = os.path.join(SKILLS_DIR, "skills_db.json")
GITHUB_REPO = "https://github.com/asdlokijj9-design/clawhub-skills"

# 分类映射
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

def load_db():
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    db = load_db()
    
    # 统计
    stats_lines = ""
    for group, cats in GROUPS.items():
        count = len([s for s in db["skills"] if s["category"] in cats])
        stats_lines += f"| {group} | {count} |\n"
    
    # 详情
    details = ""
    for group, cats in GROUPS.items():
        details += f"\n### {group}\n\n"
        for cat in cats:
            skill = next((s for s in db["skills"] if s["category"] == cat), None)
            if skill:
                displayName = skill.get("displayName", skill["name"])
                desc = skill.get("description", "")[:60]
                details += f"- **{displayName}**: {desc}\n"
    
    message = f"""# ClawHub Skills 同步报告

**同步时间:** {db['last_sync']}

---

## 统计概览

| 分类 | 数量 |
|------|------|
{stats_lines}| **总计** | **{len(db['skills'])}** |

---

## 分类详情{details}

---

## 链接

- **GitHub:** {GITHUB_REPO}
- **官网:** https://www.clawhub.ai/skills

---
*每天 10:00 自动同步*"""
    
    # 保存
    msg_file = os.path.join(SKILLS_DIR, "feishu_notification.md")
    with open(msg_file, 'w', encoding='utf-8') as f:
        f.write(message)
    
    print(message)
    print()
    print(f"已保存: {msg_file}")

if __name__ == '__main__':
    main()
