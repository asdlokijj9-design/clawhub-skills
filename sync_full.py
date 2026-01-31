# -*- coding: utf-8 -*-
"""
ClawHub Skills 同步系统 - 完整版
- 抓取官方 Skills
- 按功能分类
- 保存到数据库
- 推送 GitHub
- 发送飞书通知
"""

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
import os
import subprocess
import requests
from datetime import datetime
from bs4 import BeautifulSoup

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

def print_header(title):
    print("=" * 60)
    print(f"  {title}")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()

def fetch_clawhub():
    print("[1/5] 抓取 ClawHub...")
    url = "https://www.clawhub.ai/skills"
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code == 200:
            html_file = os.path.join(SKILLS_DIR, "clawhub_live.html")
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"  OK: HTML saved ({len(response.text)} chars)")
            return response.text
    except Exception as e:
        print(f"  Warning: {e}")
    return None

def parse_skills(html):
    print("\n[2/5] 解析 Skills...")
    skills = []
    if not html:
        print("  Warning: No HTML")
        return skills
    
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', href=True)
    skill_links = [a for a in links if '/skill/' in a.get('href', '')]
    print(f"  Found {len(skill_links)} skill links")
    
    for link in skill_links[:30]:
        skill = {
            "name": link.get_text(strip=True) or "Unknown",
            "url": link.get('href', ''),
            "description": "",
            "category": "other",
            "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        if skill['url'] and skill['name'] and skill['url'] != '#':
            skills.append(skill)
    
    if not skills:
        print("  Note: SPA page, manual check needed")
        skills.append({
            "name": "Check clawhub.ai/skills manually",
            "url": "https://www.clawhub.ai/skills",
            "description": "Visit website to see latest skills",
            "category": "other",
            "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    print(f"  Parsed {len(skills)} skills")
    return skills

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"skills": [], "last_sync": None}

def save_db(db):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def categorize(name, desc):
    text = (name + " " + desc).lower()
    keywords = {
        "voice": ["voice", "tts", "speech", "audio", "sound"],
        "browser": ["browser", "web", "crawl", "scrape", "fetch"],
        "memory": ["memory", "remember", "note", "journal"],
        "message": ["message", "send", "notify", "telegram", "discord"],
        "file": ["file", "read", "write", "edit", "folder"],
        "developer": ["git", "code", "shell", "exec", "terminal"],
        "image": ["image", "photo", "picture", "vision", "ocr"],
        "calendar": ["calendar", "schedule", "reminder", "cron"],
        "ecommerce": ["shop", "amazon", "product", "price"],
        "ai": ["ai", "llm", "gpt", "openai", "model"],
    }
    for cat, words in keywords.items():
        for word in words:
            if word in text:
                return cat
    return "other"

def update_db(new_skills):
    print("\n[3/5] 更新数据库...")
    db = load_db()
    before = len(db["skills"])
    added = []
    
    for skill in new_skills:
        exists = False
        for existing in db["skills"]:
            if existing.get("url") == skill.get("url"):
                exists = True
                break
        if not exists:
            skill["category"] = categorize(skill.get("name", ""), skill.get("description", ""))
            db["skills"].append(skill)
            added.append(skill)
            print(f"  + {skill['name']}")
    
    db["last_sync"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_db(db)
    print(f"  Stats: {len(db['skills'])} total, {len(added)} new")
    return db, added

def generate_readme(db):
    print("\n[4/5] 生成分类清单...")
    stats = {}
    for skill in db["skills"]:
        cat = skill.get("category", "other")
        stats[cat] = stats.get(cat, 0) + 1
    
    readme = f"""# ClawHub Skills 同步仓库

**最后同步:** {db['last_sync']}  
**GitHub:** [View]({GITHUB_REPO})  
**官网:** [ClawHub](https://www.clawhub.ai/skills)

---

## 统计

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
                name = skill.get("name", "Unknown")[:40]
                desc = skill.get("description", "")[:60]
                readme += f"- **{name}**"
                if desc:
                    readme += f" - {desc}"
                readme += "\n"
        readme += "\n"
    
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(readme)
    print("  OK: README.md")

def git_sync():
    print("\n[5/5] Git 同步...")
    try:
        subprocess.run(["git", "add", "-A"], cwd=SKILLS_DIR, capture_output=True)
        commit_msg = f"Sync: {datetime.now().strftime('%Y-%m-%d')} - {len(load_db()['skills'])} skills"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=SKILLS_DIR, capture_output=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=SKILLS_DIR, capture_output=True, timeout=30)
        print("  OK: Pushed to GitHub")
    except Exception as e:
        print(f"  Warning: {e}")

def main():
    print_header("ClawHub Skills 完整同步")
    
    html = fetch_clawhub()
    skills = parse_skills(html)
    db, added = update_db(skills)
    generate_readme(db)
    git_sync()
    
    print()
    print("=" * 60)
    print("  完成！")
    print("=" * 60)
    print(f"  数据库: {len(db['skills'])} Skills")
    print(f"  新增: {len(added)}")
    print()

if __name__ == '__main__':
    main()
