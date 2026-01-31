# -*- coding: utf-8 -*-
"""
生成飞书通知消息
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

def load_db():
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_feishu_message(db):
    """生成飞书 Markdown 消息"""
    
    stats = {}
    for skill in db["skills"]:
        cat = skill.get("category", "other")
        stats[cat] = stats.get(cat, 0) + 1
    
    total = len(db["skills"])
    
    # 分类统计
    stats_lines = ""
    for cat in sorted(stats.keys()):
        cat_name = CATEGORY_MAP.get(cat, cat)
        count = stats[cat]
        stats_lines += f"| {cat_name} | {count} |\n"
    
    # 分类详情
    details = ""
    for cat in sorted(stats.keys()):
        cat_name = CATEGORY_MAP.get(cat, cat)
        details += f"\n### {cat_name}\n\n"
        for skill in db["skills"]:
            if skill.get("category") == cat:
                name = skill.get("name", "Unknown")
                desc = skill.get("description", "")[:50]
                url = skill.get("url", "")
                if desc:
                    details += f"- **{name}** - {desc}"
                else:
                    details += f"- **{name}**"
                if url:
                    details += f" ([链接]({url}))"
                details += "\n"
    
    message = f"""# 📦 ClawHub Skills 同步报告

**同步时间:** {db['last_sync']}

---

## 📊 数据库统计

| 分类 | 数量 |
|------|------|
{stats_lines}| **总计** | **{total}** |

---

## 📦 分类详情{details}

---

## 🔗 链接

- **GitHub 仓库:** {GITHUB_REPO}
- **官网:** https://www.clawhub.ai/skills
- **分类清单:** [README.md]({GITHUB_REPO}/blob/main/README.md)
"""
    
    return message

def main():
    print("=" * 60)
    print("  生成飞书通知消息")
    print("=" * 60)
    print()
    
    db = load_db()
    message = generate_feishu_message(db)
    
    # 保存消息
    msg_file = os.path.join(SKILLS_DIR, "feishu_notification.md")
    with open(msg_file, 'w', encoding='utf-8') as f:
        f.write(message)
    
    print(f"  消息已保存: {msg_file}")
    print(f"  字符数: {len(message)}")
    print()
    
    # 输出消息内容
    print(message)
    
    print()
    print("=" * 60)
    print("  消息生成完成！")
    print("=" * 60)

if __name__ == '__main__':
    main()
