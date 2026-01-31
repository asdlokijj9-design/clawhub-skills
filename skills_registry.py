# -*- coding: utf-8 -*-
"""
ClawHub Skills 分类系统 - 精细版
根据具体功能和名称进行分类
"""

from datetime import datetime

# 完整 Skills 列表（含详细分类）
ALL_SKILLS = [
    # ==================== 通用能力 ====================
    {
        "name": "voice-activation",
        "displayName": "语音唤醒",
        "description": "语音唤醒词检测，支持自定义关键词",
        "category": "voice-activation",
        "subcategory": "语音交互",
        "tags": ["voice", "wake", "microphone"]
    },
    {
        "name": "text-to-speech",
        "displayName": "文字转语音 (TTS)",
        "description": "将文本转换为语音并返回 MEDIA 路径",
        "category": "text-to-speech",
        "subcategory": "语音交互",
        "tags": ["voice", "tts", "audio"]
    },
    {
        "name": "image-analysis",
        "displayName": "图像分析",
        "description": "使用配置的图像模型分析图像内容",
        "category": "image-analysis",
        "subcategory": "AI分析",
        "tags": ["image", "vision", "ai", "analysis"]
    },
    {
        "name": "web-search",
        "displayName": "网络搜索",
        "description": "使用 Brave Search API 进行网络搜索",
        "category": "web-search",
        "subcategory": "信息获取",
        "tags": ["search", "web", "brave"]
    },
    {
        "name": "web-fetch",
        "displayName": "网页内容抓取",
        "description": "从 URL 获取并提取可读内容（HTML 转 Markdown/文本）",
        "category": "web-fetch",
        "subcategory": "信息获取",
        "tags": ["fetch", "web", "crawl", "html"]
    },
    
    # ==================== 浏览器控制 ====================
    {
        "name": "browser-control",
        "displayName": "浏览器控制",
        "description": "通过 OpenClaw 浏览器控制服务控制浏览器（导航、点击、截图等）",
        "category": "browser-control",
        "subcategory": "浏览器自动化",
        "tags": ["browser", "automation", "ui"]
    },
    
    # ==================== 记忆管理 ====================
    {
        "name": "memory-management",
        "displayName": "记忆管理",
        "description": "语义搜索和读取记忆文件（MEMORY.md, memory/*.md）",
        "category": "memory-management",
        "subcategory": "知识管理",
        "tags": ["memory", "semantic", "search"]
    },
    
    # ==================== 文件与存储 ====================
    {
        "name": "file-operations",
        "displayName": "文件操作",
        "description": "读取、写入、编辑文件内容",
        "category": "file-operations",
        "subcategory": "文件系统",
        "tags": ["file", "read", "write", "edit"]
    },
    {
        "name": "shell-execution",
        "displayName": "Shell 命令执行",
        "description": "执行 Shell 命令，支持 PTY、后台运行和超时控制",
        "category": "shell-execution",
        "subcategory": "命令行",
        "tags": ["shell", "exec", "terminal", "cmd"]
    },
    
    # ==================== 消息与通信 ====================
    {
        "name": "bluebubbles",
        "displayName": "BlueBubbles 消息",
        "description": "BlueBubbles 外部频道插件，支持 REST API 发送/探测和 Webhook 接收",
        "category": "bluebubbles",
        "subcategory": "消息渠道",
        "tags": ["message", "api", "webhook"]
    },
    {
        "name": "session-management",
        "displayName": "会话管理",
        "description": "列出、发送消息和获取其他会话/子代理的历史",
        "category": "session-management",
        "subcategory": "会话控制",
        "tags": ["session", "history", "sub-agent"]
    },
    
    # ==================== 定时任务 ====================
    {
        "name": "cron-scheduler",
        "displayName": "定时任务调度",
        "description": "管理 Gateway 定时任务和唤醒事件",
        "category": "cron-scheduler",
        "subcategory": "系统调度",
        "tags": ["cron", "schedule", "reminder"]
    },
    
    # ==================== 系统管理 ====================
    {
        "name": "gateway-management",
        "displayName": "Gateway 管理",
        "description": "重启、配置或更新 Gateway 服务",
        "category": "gateway-management",
        "subcategory": "系统管理",
        "tags": ["gateway", "restart", "config"]
    },
    {
        "name": "canvas-control",
        "displayName": "画布控制",
        "description": "控制节点画布（呈现/隐藏/截图/A2UI）",
        "category": "canvas-control",
        "subcategory": "节点控制",
        "tags": ["canvas", "ui", "presentation"]
    },
    {
        "name": "node-control",
        "displayName": "节点控制",
        "description": "发现和控制配对节点（状态/描述/相机/屏幕/位置/运行）",
        "category": "node-control",
        "subcategory": "节点控制",
        "tags": ["node", "device", "camera", "screen"]
    },
    
    # ==================== 开发者工具 ====================
    {
        "name": "skill-creator",
        "displayName": "Skill 创建器",
        "description": "创建或更新 AgentSkills，包含脚本、引用和资源",
        "category": "skill-creator",
        "subcategory": "开发工具",
        "tags": ["skill", "create", "agent"]
    },
    
    # ==================== 飞书集成 ====================
    {
        "name": "feishu-doc",
        "displayName": "飞书文档",
        "description": "飞书文档操作（创建/读取/写入/更新/删除/追加）",
        "category": "feishu-doc",
        "subcategory": "飞书集成",
        "tags": ["feishu", "document", "doc"]
    },
    {
        "name": "feishu-app",
        "displayName": "飞书应用",
        "description": "列出当前飞书应用权限（Scopes），用于调试权限问题",
        "category": "feishu-app",
        "subcategory": "飞书集成",
        "tags": ["feishu", "permission", "scope"]
    },
    {
        "name": "feishu-folder",
        "displayName": "飞书文件夹",
        "description": "列出飞书文件夹中的文档和子文件夹",
        "category": "feishu-folder",
        "subcategory": "飞书集成",
        "tags": ["feishu", "folder", "list"]
    },
]

# 分类映射（显示名称）
CATEGORIES = {
    # 一级分类
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

def get_skills():
    return ALL_SKILLS

def main():
    print("=" * 60)
    print("  ClawHub Skills 精细分类系统")
    print("=" * 60)
    print()
    
    print(f"总 Skills 数量: {len(ALL_SKILLS)}")
    print()
    
    # 显示分组统计
    for group, cats in GROUPS.items():
        count = len([s for s in ALL_SKILLS if s["category"] in cats])
        print(f"\n【{group}】({count} 个)")
        for cat in cats:
            skill = next((s for s in ALL_SKILLS if s["category"] == cat), None)
            if skill:
                print(f"  - {skill['displayName']} - {skill['description'][:50]}...")
    
    print()
    print("=" * 60)
    print(f"总计: {len(ALL_SKILLS)} 个 Skills")
    print("=" * 60)

if __name__ == '__main__':
    main()
