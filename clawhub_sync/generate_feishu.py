# -*- coding: utf-8 -*-
"""
ClawHub Skills 飞书文档生成器
生成飞书文档格式的 Skills 列表
"""

import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
from datetime import datetime
from typing import List, Dict

# 导入 Skills 数据
from known_skills import KNOWN_SKILLS, get_all_skills, get_stats

class FeishuDocGenerator:
    """飞书文档生成器"""
    
    def __init__(self):
        self.stats = get_stats()
    
    def generate_header(self) -> str:
        """生成文档标题"""
        return f"""# 🦞 ClawHub Skills 完整索引

> 数据来源: [clawhub.ai/skills](https://clawhub.ai/skills)  
> 更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
> 总 Skills: {sum(self.stats.values())} | 分类: {len(self.stats)}

---

## 📊 分类统计

| 分类 | 数量 |
|------|------|
"""
    
    def generate_stats_table(self) -> str:
        """生成统计表格"""
        table = ""
        for cat, count in sorted(self.stats.items(), key=lambda x: -x[1]):
            table += f"| {cat} | {count} |\n"
        return table
    
    def generate_category_section(self, category: str, skills: List[Dict]) -> str:
        """生成分类部分"""
        section = f"\n## {category}\n\n"
        
        for skill in skills:
            section += f"### {skill['displayName']}\n\n"
            section += f"- **描述**: {skill['description']}\n"
            section += f"- **标签**: {' '.join([f'`{tag}`' for tag in skill.get('tags', [])])}\n"
            section += f"- **标识符**: `{skill['name']}`\n\n"
        
        return section
    
    def generate_full_doc(self) -> str:
        """生成完整文档"""
        doc = self.generate_header()
        doc += self.generate_stats_table()
        
        # 按分类生成
        for category, skills in sorted(KNOWN_SKILLS.items(), key=lambda x: -self.stats.get(x[0], 0)):
            doc += self.generate_category_section(category, skills)
        
        # 附录
        doc += f"""
---

## 📝 附录

### 使用说明

```bash
# 搜索 Skills
clawhub skills search <关键词>

# 安装 Skills
clawhub skills install <skill-name>

# 列出分类
clawhub skills list --category finance
```

### 更新日志

- **v1.0.0** (2026-02-01): 初始版本，收录 {sum(self.stats.values())} 个 Skills

---

*💡 提示: 使用 `clawhub skills` 命令管理 Skills*
"""
        
        return doc
    
    def generate_compact_doc(self) -> str:
        """生成简洁版本"""
        doc = f"# ClawHub Skills ({sum(self.stats.values())})\n\n"
        doc += f"*{datetime.now().strftime('%Y-%m-%d')}*\n\n"
        
        for category, skills in sorted(KNOWN_SKILLS.items(), key=lambda x: -len(x[1])):
            doc += f"### {category}\n"
            for skill in skills[:5]:  # 每个分类只显示前5个
                doc += f"- **{skill['displayName']}**: {skill['description']}\n"
            if len(skills) > 5:
                doc += f"- ... 还有 {len(skills) - 5} 个\n"
            doc += "\n"
        
        return doc
    
    def generate_json_for_feishu(self) -> str:
        """生成飞书 JSON 格式"""
        data = {
            "title": "ClawHub Skills 完整索引",
            "blocks": []
        }
        
        # 标题
        data["blocks"].append({
            "type": "heading1",
            "heading1": {"elements": [{"type": "text", "text": "🦞 ClawHub Skills 完整索引"}]}
        })
        
        # 描述
        data["blocks"].append({
            "type": "text",
            "text": {"elements": [
                {"type": "text", "text": f"收录 {sum(self.stats.values())} 个 Skills，涵盖 {len(self.stats)} 个分类"}
            ]}
        })
        
        # 分类标题
        for category, skills in sorted(KNOWN_SKILLS.items(), key=lambda x: -len(x[1])):
            data["blocks"].append({
                "type": "heading2",
                "heading2": {"elements": [{"type": "text", "text": category}]}
            })
            
            # 技能列表
            for skill in skills:
                data["blocks"].append({
                    "type": "text",
                    "text": {"elements": [
                        {"type": "text", "text": f"• {skill['displayName']}: {skill['description']}"}
                    ]}
                })
        
        return json.dumps(data, ensure_ascii=False, indent=2)
    
    def save_to_file(self, filename: str = "clawhub_skills_feishu.md"):
        """保存到文件"""
        content = self.generate_full_doc()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ 已保存到 {filename}")
        
        # 保存简洁版
        compact_filename = filename.replace(".md", "_compact.md")
        content = self.generate_compact_doc()
        with open(compact_filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ 已保存简洁版到 {compact_filename}")
        
        # 保存 JSON
        json_filename = filename.replace(".md", ".json")
        content = self.generate_json_for_feishu()
        with open(json_filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ 已保存 JSON 到 {json_filename}")
    
    def print_summary(self):
        """打印摘要"""
        print(f"\n📦 收录 {sum(self.stats.values())} 个 Skills")
        print(f"📂 分类: {len(self.stats)} 个\n")
        
        for cat, count in sorted(self.stats.items(), key=lambda x: -x[1]):
            print(f"  {cat}: {count}")

def main():
    """主函数"""
    generator = FeishuDocGenerator()
    generator.print_summary()
    
    print("\n📄 生成文档...")
    generator.save_to_file()
    
    print("\n✅ 完成!")

if __name__ == "__main__":
    main()
