# -*- coding: utf-8 -*-
"""
ClawHub Skills 每日同步脚本
每天 10:00 自动执行
"""

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
import os
import subprocess
from datetime import datetime

# 配置
SKILLS_DIR = r"D:\moltbot开发项目\06_待优化方案\clawhub_skills"
CLAWHUB_URL = "https://www.clawhub.ai/skills"
DB_FILE = os.path.join(SKILLS_DIR, "skills_db.json")
README_FILE = os.path.join(SKILLS_DIR, "README.md")
CHANGELOG_FILE = os.path.join(SKILLS_DIR, "CHANGELOG.md")
RAW_HTML_FILE = os.path.join(SKILLS_DIR, "clawhub_raw.html")

# 功能分类
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

def print_header():
    print("=" * 50)
    print("  ClawHub Skills Daily Sync")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    print()

def load_db():
    """加载数据库"""
    if not os.path.exists(SKILLS_DIR):
        os.makedirs(SKILLS_DIR, exist_ok=True)
    
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"skills": [], "last_sync": None}

def save_db(db):
    """保存数据库"""
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def categorize(name, desc):
    """根据名称和描述分类"""
    text = (name + " " + desc).lower()
    
    keywords = {
        "voice": ["voice", "tts", "speech", "audio", "sound"],
        "browser": ["browser", "web", "crawl", "scrape", "fetch"],
        "memory": ["memory", "remember", "note", "journal", "log"],
        "message": ["message", "send", "notify", "telegram", "discord", "whatsapp", "signal"],
        "file": ["file", "read", "write", "edit", "folder", "path"],
        "developer": ["git", "code", "shell", "exec", "terminal", "cmd"],
        "image": ["image", "photo", "picture", "vision", "ocr", "picture"],
        "calendar": ["calendar", "schedule", "reminder", "cron", "event"],
        "ecommerce": ["shop", "amazon", "taobao", "jd", "product", "price", "shopify"],
        "ai": ["ai", "llm", "gpt", "openai", "anthropic", "model", "embedding"],
    }
    
    for cat, words in keywords.items():
        for word in words:
            if word in text:
                return cat
    return "other"

def fetch_website():
    """抓取网站"""
    print("[1/5] Fetching ClawHub...")
    
    try:
        import requests
        response = requests.get(CLAWHUB_URL, timeout=15)
        if response.status_code == 200:
            with open(RAW_HTML_FILE, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"  OK: HTML saved ({len(response.text)} chars)")
            return True
    except Exception as e:
        print(f"  Warning: {e}")
    
    print("  Note: Page uses JavaScript, manual check may be needed")
    return False

def parse_skills():
    """解析 Skills"""
    print("\n[2/5] Parsing Skills...")
    
    new_skills = []
    
    if os.path.exists(RAW_HTML_FILE):
        with open(RAW_HTML_FILE, 'r', encoding='utf-8') as f:
            html = f.read()
        
        print(f"  HTML loaded: {len(html)} chars")
        
        # 由于页面是 SPA，需要 Playwright 完整解析
        # 这里提供手动检查的提示
        print("  Note: SPA page, full parsing needs Playwright")
        
        # 添加占位符（实际使用时请更新）
        new_skills.append({
            "name": "New Skill (Manual Check Needed)",
            "description": f"Please check {CLAWHUB_URL} for updates",
            "url": CLAWHUB_URL,
            "category": "other",
            "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    else:
        print("  Warning: No HTML file found")
    
    return new_skills

def update_db(new_skills):
    """更新数据库"""
    print("\n[3/5] Updating Database...")
    
    db = load_db()
    before_count = len(db["skills"])
    added = 0
    
    for skill in new_skills:
        # 检查是否已存在
        exists = False
        for existing in db["skills"]:
            if existing.get("url") == skill.get("url"):
                exists = True
                break
        
        if not exists:
            # 分类
            skill["category"] = categorize(skill.get("name", ""), skill.get("description", ""))
            db["skills"].append(skill)
            added += 1
            print(f"  + {skill['name']}")
    
    db["last_sync"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_db(db)
    
    print(f"  Stats: {len(db['skills'])} total ({added} new)")
    return db

def generate_readme(db):
    """生成分类清单"""
    print("\n[4/5] Generating README...")
    
    # 统计分类
    stats = {}
    for skill in db["skills"]:
        cat = skill.get("category", "other")
        stats[cat] = stats.get(cat, 0) + 1
    
    # 生成 README
    readme = f"""# ClawHub Skills Sync Repository

**Last Sync:** {db['last_sync']}  
**Source:** [ClawHub]({CLAWHUB_URL})

---

## Statistics

| Category | Count |
|----------|-------|
"""
    
    total = 0
    for cat in sorted(stats.keys()):
        cat_name = CATEGORY_MAP.get(cat, cat)
        count = stats[cat]
        total += count
        readme += f"| {cat_name} | {count} |\n"
    
    readme += f"| **Total** | **{total}** |\n"
    readme += "\n---\n\n## Category Details\n\n"
    
    for cat in sorted(stats.keys()):
        cat_name = CATEGORY_MAP.get(cat, cat)
        readme += f"### {cat_name}\n\n"
        
        for skill in db["skills"]:
            if skill.get("category") == cat:
                desc = skill.get("description", "")[:80]
                if len(skill.get("description", "")) > 80:
                    desc += "..."
                readme += f"- **{skill['name']}** - {desc}\n"
        readme += "\n"
    
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(readme)
    
    print(f"  OK: {README_FILE}")

def git_sync():
    """Git 同步"""
    print("\n[5/5] Git Sync...")
    
    # 检查 Token
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        print("  Warning: GITHUB_TOKEN not set")
        print("  Run setup_github.ps1 to configure")
        return
    
    # 初始化 git（如果需要）
    git_dir = os.path.join(SKILLS_DIR, ".git")
    if not os.path.exists(git_dir):
        try:
            subprocess.run(["git", "init"], cwd=SKILLS_DIR, capture_output=True)
            subprocess.run(["git", "config", "user.name", "Moltbot User"], cwd=SKILLS_DIR, capture_output=True)
            subprocess.run(["git", "config", "user.email", "asdlokijj9@gmail.com"], cwd=SKILLS_DIR, capture_output=True)
            print("  OK: Git repository initialized")
        except Exception as e:
            print(f"  Error: {e}")
            return
    
    try:
        subprocess.run(["git", "add", "-A"], cwd=SKILLS_DIR, capture_output=True)
        commit_msg = f"Sync: {datetime.now().strftime('%Y-%m-%d')}"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=SKILLS_DIR, capture_output=True)
        print(f"  OK: Committed ({commit_msg})")
    except Exception as e:
        print(f"  Warning: {e}")

def main():
    print_header()
    
    # 1. 抓取
    fetch_website()
    
    # 2. 解析
    new_skills = parse_skills()
    
    # 3. 更新数据库
    db = update_db(new_skills)
    
    # 4. 生成清单
    generate_readme(db)
    
    # 5. Git 同步
    git_sync()
    
    print()
    print("=" * 50)
    print("  Sync Complete!")
    print("=" * 50)
    print()
    print("Files:")
    print(f"  - DB: {DB_FILE}")
    print(f"  - README: {README_FILE}")
    print()

if __name__ == '__main__':
    main()
