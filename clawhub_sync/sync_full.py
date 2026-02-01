# -*- coding: utf-8 -*-
"""
ClawHub Skills 同步工具
自动从 clawhub.ai 抓取最新 Skills 列表
"""

import asyncio
import aiohttp
import json
import re
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
import hashlib

@dataclass
class Skill:
    name: str
    display_name: str
    description: str
    category: str
    tags: List[str]
    downloads: int
    rating: float
    author: str
    updated: str

class ClawHubSync:
    """ClawHub Skills 同步器"""
    
    BASE_URL = "https://clawhub.ai"
    API_URL = f"{BASE_URL}/api/skills"
    
    CATEGORIES = {
        "finance": ["股票", "加密货币", "支付", "预算", "税务", "投资", "交易", "钱包"],
        "communication": ["消息", "邮件", "Telegram", "Discord", "Slack", "通知", "日历"],
        "notes": ["笔记", "文档", "知识管理", "PDF", "书签", "Obsidian", "Notion"],
        "developer": ["Git", "代码", "开发", "API", "数据库", "测试", "CI/CD"],
        "media": ["视频", "音频", "图像", "转录", "截图", "播客"],
        "automation": ["自动化", "定时", "工作流", "触发器", "批量"],
        "system": ["系统", "监控", "日志", "备份", "进程", "安全"],
        "ai": ["AI", "ML", "LLM", "模型", "RAG", "嵌入", "代理"],
        "data": ["数据", "搜索", "缓存", "ETL", "查询", "转换"],
        "design": ["UI", "设计", "组件", "动画", "主题"],
        "devops": ["Docker", "K8s", "部署", "监控", "密钥", "负载均衡"],
        "other": []
    }
    
    def __init__(self, output_dir: str = "skills_data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.skills: List[Skill] = []
    
    def classify_category(self, text: str) -> str:
        """根据文本内容分类"""
        text = text.lower()
        for category, keywords in self.CATEGORIES.items():
            for keyword in keywords:
                if keyword.lower() in text:
                    return category
        return "other"
    
    async def fetch_skills(self, session: aiohttp.ClientSession) -> List[Dict]:
        """获取 Skills 列表"""
        try:
            async with session.get(self.API_URL, timeout=30) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("skills", [])
        except Exception as e:
            print(f"API 请求失败: {e}")
        
        # 如果 API 失败，返回预设数据
        return self.get_fallback_skills()
    
    def get_fallback_skills(self) -> List[Dict]:
        """预设的 Skills 列表"""
        return [
            {"name": "yahoo-finance", "display_name": "Yahoo Finance", "description": "股票价格查询与实时数据"},
            {"name": "polymarket-trading-bot", "display_name": "Polymarket交易机器人", "description": "预测市场交易分析"},
            {"name": "binance-api", "display_name": "Binance API", "description": "加密货币交易接口"},
            {"name": "stripe-integration", "display_name": "Stripe集成", "description": "支付处理"},
            {"name": "paypal-cli", "displayName": "PayPal CLI", "description": "PayPal管理"},
            {"name": "gmail-search", "displayName": "Gmail搜索", "description": "邮件搜索"},
            {"name": "discord-bot", "displayName": "Discord机器人", "description": "Discord通知"},
            {"name": "telegram-bot", "displayName": "Telegram机器人", "description": "Telegram自动化"},
            {"name": "notion-sync", "displayName": "Notion同步", "description": "双向同步"},
            {"name": "obsidian-link", "displayName": "Obsidian链接", "description": "知识图谱"},
            {"name": "github-cli", "displayName": "GitHub CLI", "description": "版本控制"},
            {"name": "docker-compose", "displayName": "Docker编排", "description": "容器编排"},
            {"name": "youtube-transcript", "displayName": "YouTube转录", "description": "视频转文字"},
            {"name": "audio-transcribe", "displayName": "语音转文字", "description": "Whisper转录"},
            {"name": "cron-scheduler", "displayName": "定时任务", "description": "Cron调度"},
            {"name": "system-monitor", "displayName": "系统监控", "description": "CPU/内存监控"},
            {"name": "model-manager", "displayName": "模型管理", "description": "LLM切换"},
            {"name": "rag-system", "displayName": "RAG系统", "description": "知识增强"},
            {"name": "database-query", "displayName": "数据库查询", "description": "SQL执行"},
            {"name": "ui-component", "displayName": "UI组件", "description": "React/Vue组件"},
        ]
    
    def parse_skill(self, raw: Dict) -> Skill:
        """解析原始数据为 Skill 对象"""
        description = raw.get("description", "")
        if not description:
            description = raw.get("summary", "")
        
        return Skill(
            name=raw.get("name", raw.get("slug", "")),
            display_name=raw.get("display_name", raw.get("title", raw.get("name", ""))),
            description=description,
            category=self.classify_category(description),
            tags=raw.get("tags", []),
            downloads=raw.get("downloads", 0),
            rating=raw.get("rating", 0.0),
            author=raw.get("author", ""),
            updated=raw.get("updated", "")
        )
    
    async def sync(self) -> List[Skill]:
        """执行同步"""
        print("🔄 开始同步 ClawHub Skills...")
        
        async with aiohttp.ClientSession() as session:
            raw_skills = await self.fetch_skills(session)
        
        self.skills = [self.parse_skill(s) for s in raw_skills]
        
        print(f"✅ 同步完成: {len(self.skills)} 个 Skills")
        
        # 保存数据
        self.save()
        
        return self.skills
    
    def save(self):
        """保存到文件"""
        # 保存 JSON
        json_path = self.output_dir / "skills.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump([asdict(s) for s in self.skills], f, ensure_ascii=False, indent=2)
        
        # 保存统计
        stats = self.get_stats()
        stats_path = self.output_dir / "stats.json"
        with open(stats_path, "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        
        print(f"💾 数据已保存到 {self.output_dir}")
    
    def get_stats(self) -> Dict:
        """获取统计信息"""
        stats = {"total": len(self.skills), "categories": {}}
        for skill in self.skills:
            cat = skill.category
            stats["categories"][cat] = stats["categories"].get(cat, 0) + 1
        return stats
    
    def search(self, keyword: str) -> List[Skill]:
        """搜索 Skills"""
        keyword = keyword.lower()
        return [
            s for s in self.skills
            if keyword in s.display_name.lower()
            or keyword in s.description.lower()
            or keyword in s.name.lower()
        ]
    
    def filter_by_category(self, category: str) -> List[Skill]:
        """按分类筛选"""
        return [s for s in self.skills if s.category == category]

async def main():
    """主函数"""
    sync = ClawHubSync()
    skills = await sync.sync()
    
    # 打印统计
    stats = sync.get_stats()
    print(f"\n📊 统计:")
    print(f"  总数: {stats['total']}")
    for cat, count in sorted(stats["categories"].items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")
    
    # 示例搜索
    print(f"\n🔍 搜索 'finance':")
    results = sync.search("finance")[:5]
    for s in results:
        print(f"  - {s.display_name}: {s.description}")

if __name__ == "__main__":
    asyncio.run(main())
