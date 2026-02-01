# -*- coding: utf-8 -*-
"""
已知 ClawHub Skills 完整列表
从 clawhub.ai/skills 收录
"""

KNOWN_SKILLS = {
    # ========== 金融与交易 ==========
    "finance": [
        {
            "name": "yahoo-finance",
            "displayName": "Yahoo Finance",
            "description": "股票价格查询与实时数据",
            "tags": ["股票", "金融", "价格"]
        },
        {
            "name": "polymarket-trading-bot",
            "displayName": "Polymarket交易机器人",
            "description": "预测市场交易分析",
            "tags": ["交易", "预测市场"]
        },
        {
            "name": "binance-api",
            "displayName": "Binance API",
            "description": "加密货币交易接口",
            "tags": ["加密货币", "交易"]
        },
        {
            "name": "stripe-integration",
            "displayName": "Stripe集成",
            "description": "支付处理",
            "tags": ["支付", "Stripe"]
        },
        {
            "name": "paypal-cli",
            "displayName": "PayPal CLI",
            "description": "PayPal管理",
            "tags": ["PayPal", "支付"]
        },
        {
            "name": "budget-tracker",
            "displayName": "预算追踪",
            "description": "个人预算管理",
            "tags": ["预算", "理财"]
        },
        {
            "name": "investment-portfolio",
            "displayName": "投资组合",
            "description": "资产管理",
            "tags": ["投资", "组合"]
        },
        {
            "name": "tax-calculator",
            "displayName": "税务计算",
            "description": "税务计算器",
            "tags": ["税务", "计算"]
        },
        {
            "name": "invoice-generator",
            "displayName": "发票生成",
            "description": "账单/发票",
            "tags": ["发票", "账单"]
        },
        {
            "name": "receipt-scanner",
            "displayName": "收据扫描",
            "description": "收据OCR识别",
            "tags": ["OCR", "收据"]
        },
        {
            "name": "expense-tracker",
            "displayName": "支出追踪",
            "description": "开支记录",
            "tags": ["支出", "追踪"]
        },
        {
            "name": "crypto-wallet",
            "displayName": "加密货币钱包",
            "description": "钱包管理",
            "tags": ["加密货币", "钱包"]
        },
        {
            "name": "stock-market",
            "displayName": "股票市场",
            "description": "股市数据",
            "tags": ["股票", "市场"]
        },
        {
            "name": "forex-rates",
            "displayName": "外汇汇率",
            "description": "汇率查询",
            "tags": ["外汇", "汇率"]
        },
        {
            "name": "credit-score",
            "displayName": "信用评分",
            "description": "信用查询",
            "tags": ["信用", "评分"]
        },
    ],
    
    # ========== 消息与通讯 ==========
    "communication": [
        {
            "name": "discord-bot",
            "displayName": "Discord机器人",
            "description": "Discord通知",
            "tags": ["Discord", "消息"]
        },
        {
            "name": "telegram-bot",
            "displayName": "Telegram机器人",
            "description": "Telegram自动化",
            "tags": ["Telegram", "机器人"]
        },
        {
            "name": "gmail-search",
            "displayName": "Gmail搜索",
            "description": "邮件搜索",
            "tags": ["Gmail", "邮件"]
        },
        {
            "name": "slack-integration",
            "displayName": "Slack集成",
            "description": "Slack通知",
            "tags": ["Slack", "团队"]
        },
        {
            "name": "whatsapp-bot",
            "displayName": "WhatsApp机器人",
            "description": "WhatsApp自动化",
            "tags": ["WhatsApp", "消息"]
        },
        {
            "name": "email-automation",
            "displayName": "邮件自动化",
            "description": "IMAP/SMTP",
            "tags": ["邮件", "自动化"]
        },
        {
            "name": "calendar-reminder",
            "displayName": "日历提醒",
            "description": "日程提醒",
            "tags": ["日历", "提醒"]
        },
        {
            "name": "webhook-handler",
            "displayName": "Webhook处理器",
            "description": "API回调",
            "tags": ["Webhook", "回调"]
        },
        {
            "name": "notification-center",
            "displayName": "通知中心",
            "description": "多渠道通知",
            "tags": ["通知", "中心"]
        },
        {
            "name": "sms-sender",
            "displayName": "短信发送",
            "description": "短信通知",
            "tags": ["短信", "SMS"]
        },
        {
            "name": "push-notification",
            "displayName": "推送通知",
            "description": "移动推送",
            "tags": ["推送", "通知"]
        },
        {
            "name": "voice-call",
            "displayName": "语音通话",
            "description": "电话通知",
            "tags": ["语音", "电话"]
        },
    ],
    
    # ========== 笔记与知识管理 ==========
    "notes": [
        {
            "name": "notion-sync",
            "displayName": "Notion同步",
            "description": "双向同步",
            "tags": ["Notion", "同步"]
        },
        {
            "name": "obsidian-link",
            "displayName": "Obsidian链接",
            "description": "知识图谱",
            "tags": ["Obsidian", "知识"]
        },
        {
            "name": "bear-notes",
            "displayName": "Bear笔记",
            "description": "Markdown笔记",
            "tags": ["Bear", "笔记"]
        },
        {
            "name": "apple-notes-app",
            "displayName": "苹果备忘录",
            "description": "备忘录管理",
            "tags": ["Apple", "备忘录"]
        },
        {
            "name": "readwise-integration",
            "displayName": "Readwise集成",
            "description": "高亮标注",
            "tags": ["Readwise", "标注"]
        },
        {
            "name": "bookmark-manager",
            "displayName": "书签管理",
            "description": "浏览器书签",
            "tags": ["书签", "管理"]
        },
        {
            "name": "pdf-annotation",
            "displayName": "PDF批注",
            "description": "批注工具",
            "tags": ["PDF", "批注"]
        },
        {
            "name": "mind-map-creator",
            "displayName": "思维导图",
            "description": "导图生成",
            "tags": ["思维导图", "图表"]
        },
        {
            "name": "local-search",
            "displayName": "本地搜索",
            "description": "全文搜索",
            "tags": ["搜索", "本地"]
        },
        {
            "name": "context-search",
            "displayName": "语义搜索",
            "description": "向量搜索",
            "tags": ["语义", "向量"]
        },
        {
            "name": "evernote-sync",
            "displayName": "印象笔记同步",
            "description": "Evernote同步",
            "tags": ["印象笔记", "同步"]
        },
        {
            "name": "notepad-plus",
            "displayName": "高级记事本",
            "description": "文本编辑",
            "tags": ["记事本", "编辑"]
        },
    ],
    
    # ========== 开发与编码 ==========
    "developer": [
        {
            "name": "github-cli",
            "displayName": "GitHub CLI",
            "description": "版本控制",
            "tags": ["GitHub", "Git"]
        },
        {
            "name": "gitlab-manage",
            "displayName": "GitLab管理",
            "description": "CI/CD管道",
            "tags": ["GitLab", "CI/CD"]
        },
        {
            "name": "docker-compose",
            "displayName": "Docker编排",
            "description": "容器编排",
            "tags": ["Docker", "容器"]
        },
        {
            "name": "k8s-deploy",
            "displayName": "Kubernetes部署",
            "description": "K8s集群管理",
            "tags": ["Kubernetes", "K8s"]
        },
        {
            "name": "code-review-bot",
            "displayName": "代码审查机器人",
            "description": "PR审查",
            "tags": ["代码审查", "PR"]
        },
        {
            "name": "test-runner",
            "displayName": "测试运行器",
            "description": "单元测试",
            "tags": ["测试", "运行"]
        },
        {
            "name": "debugger-tool",
            "displayName": "调试工具",
            "description": "调试代理",
            "tags": ["调试", "Debug"]
        },
        {
            "name": "api-documentation",
            "displayName": "API文档",
            "description": "OpenAPI规范",
            "tags": ["API", "文档"]
        },
        {
            "name": "migration-manager",
            "displayName": "迁移管理",
            "description": "数据库迁移",
            "tags": ["迁移", "数据库"]
        },
        {
            "name": "monitoring-dashboard",
            "displayName": "监控面板",
            "description": "系统监控",
            "tags": ["监控", "面板"]
        },
        {
            "name": "ssh-manager",
            "displayName": "SSH管理",
            "description": "远程连接",
            "tags": ["SSH", "远程"]
        },
        {
            "name": "terminal-shell",
            "displayName": "终端Shell",
            "description": "命令行",
            "tags": ["终端", "Shell"]
        },
        {
            "name": "json-formatter",
            "displayName": "JSON格式化",
            "description": "JSON工具",
            "tags": ["JSON", "格式化"]
        },
        {
            "name": "base64-encoder",
            "displayName": "Base64编码",
            "description": "编码解码",
            "tags": ["Base64", "编码"]
        },
        {
            "name": "regex-tester",
            "displayName": "正则测试",
            "description": "Regex测试",
            "tags": ["正则", "Regex"]
        },
    ],
    
    # ========== 媒体处理 ==========
    "media": [
        {
            "name": "youtube-transcript",
            "displayName": "YouTube转录",
            "description": "视频转文字",
            "tags": ["YouTube", "转录"]
        },
        {
            "name": "video-editor",
            "displayName": "视频剪辑",
            "description": "视频处理",
            "tags": ["视频", "剪辑"]
        },
        {
            "name": "audio-transcribe",
            "displayName": "语音转文字",
            "description": "Whisper转录",
            "tags": ["语音", "转录"]
        },
        {
            "name": "image-generator",
            "displayName": "图像生成",
            "description": "DALL-E/SD",
            "tags": ["图像", "AI"]
        },
        {
            "name": "subtitle-maker",
            "displayName": "字幕生成",
            "description": "字幕制作",
            "tags": ["字幕", "视频"]
        },
        {
            "name": "podcast-rss",
            "displayName": "播客订阅",
            "description": "RSS订阅",
            "tags": ["播客", "RSS"]
        },
        {
            "name": "screenshot-capture",
            "displayName": "截图工具",
            "description": "网页截图",
            "tags": ["截图", "屏幕"]
        },
        {
            "name": "gif-creator",
            "displayName": "GIF制作",
            "description": "动态图生成",
            "tags": ["GIF", "动图"]
        },
        {
            "name": "voice-synthesis",
            "displayName": "语音合成",
            "description": "TTS引擎",
            "tags": ["语音", "TTS"]
        },
        {
            "name": "watermark-adder",
            "displayName": "水印添加",
            "description": "版权保护",
            "tags": ["水印", "版权"]
        },
        {
            "name": "image-compressor",
            "displayName": "图片压缩",
            "description": "压缩优化",
            "tags": ["压缩", "图片"]
        },
        {
            "name": "video-compressor",
            "displayName": "视频压缩",
            "description": "视频优化",
            "tags": ["压缩", "视频"]
        },
    ],
    
    # ========== 自动化与任务 ==========
    "automation": [
        {
            "name": "cron-scheduler",
            "displayName": "定时任务",
            "description": "Cron调度",
            "tags": ["定时", "Cron"]
        },
        {
            "name": "workflow-automation",
            "displayName": "工作流自动化",
            "description": "自动化流程",
            "tags": ["工作流", "自动化"]
        },
        {
            "name": "reminder-bot",
            "displayName": "提醒机器人",
            "description": "智能提醒",
            "tags": ["提醒", "机器人"]
        },
        {
            "name": "batch-processor",
            "displayName": "批量处理",
            "description": "任务队列",
            "tags": ["批量", "处理"]
        },
        {
            "name": "trigger-handler",
            "displayName": "触发器",
            "description": "事件驱动",
            "tags": ["触发", "事件"]
        },
        {
            "name": "integration-hub",
            "displayName": "集成中心",
            "description": "API连接",
            "tags": ["集成", "API"]
        },
        {
            "name": "webhook-server",
            "displayName": "Webhook服务器",
            "description": "实时回调",
            "tags": ["Webhook", "服务器"]
        },
        {
            "name": "task-queue",
            "displayName": "任务队列",
            "description": "异步任务",
            "tags": ["队列", "异步"]
        },
        {
            "name": "retry-logic",
            "displayName": "重试机制",
            "description": "错误重试",
            "tags": ["重试", "错误"]
        },
        {
            "name": "rate-limiter",
            "displayName": "速率限制",
            "description": "API限流",
            "tags": ["限流", "速率"]
        },
    ],
    
    # ========== 系统与监控 ==========
    "system": [
        {
            "name": "system-monitor",
            "displayName": "系统监控",
            "description": "CPU/内存",
            "tags": ["系统", "监控"]
        },
        {
            "name": "log-analyzer",
            "displayName": "日志分析",
            "description": "日志搜索",
            "tags": ["日志", "分析"]
        },
        {
            "name": "backup-tool",
            "displayName": "备份工具",
            "description": "增量备份",
            "tags": ["备份", "数据"]
        },
        {
            "name": "disk-cleaner",
            "displayName": "磁盘清理",
            "description": "缓存清理",
            "tags": ["磁盘", "清理"]
        },
        {
            "name": "process-manager",
            "displayName": "进程管理",
            "description": "后台进程",
            "tags": ["进程", "管理"]
        },
        {
            "name": "health-check",
            "displayName": "健康检查",
            "description": "服务可用性",
            "tags": ["健康", "检查"]
        },
        {
            "name": "resource-monitor",
            "displayName": "资源监控",
            "description": "实时指标",
            "tags": ["资源", "监控"]
        },
        {
            "name": "security-scanner",
            "displayName": "安全扫描",
            "description": "漏洞检测",
            "tags": ["安全", "扫描"]
        },
        {
            "name": "config-updater",
            "displayName": "配置更新",
            "description": "热更新",
            "tags": ["配置", "更新"]
        },
        {
            "name": "network-speed",
            "displayName": "网络测速",
            "description": "带宽测试",
            "tags": ["网络", "速度"]
        },
    ],
    
    # ========== AI 与 机器学习 ==========
    "ai": [
        {
            "name": "model-manager",
            "displayName": "模型管理",
            "description": "LLM切换",
            "tags": ["LLM", "模型"]
        },
        {
            "name": "rag-system",
            "displayName": "RAG系统",
            "description": "知识增强",
            "tags": ["RAG", "知识"]
        },
        {
            "name": "embedding-search",
            "displayName": "向量搜索",
            "description": "语义相似",
            "tags": ["向量", "嵌入"]
        },
        {
            "name": "prompt-library",
            "displayName": "提示词库",
            "description": "模板管理",
            "tags": ["提示词", "Prompt"]
        },
        {
            "name": "fine-tuning",
            "displayName": "微调工具",
            "description": "模型微调",
            "tags": ["微调", "训练"]
        },
        {
            "name": "agent-framework",
            "displayName": "代理框架",
            "description": "多代理编排",
            "tags": ["代理", "框架"]
        },
        {
            "name": "llm-router",
            "displayName": "LLM路由",
            "description": "智能路由",
            "tags": ["路由", "LLM"]
        },
        {
            "name": "context-window",
            "displayName": "上下文窗口",
            "description": "长文本处理",
            "tags": ["上下文", "窗口"]
        },
        {
            "name": "evaluation-metrics",
            "displayName": "评估指标",
            "description": "准确度测试",
            "tags": ["评估", "指标"]
        },
        {
            "name": "token-optimizer",
            "displayName": "Token优化",
            "description": "上下文压缩",
            "tags": ["Token", "优化"]
        },
    ],
    
    # ========== 数据与搜索 ==========
    "data": [
        {
            "name": "database-query",
            "displayName": "数据库查询",
            "description": "SQL执行",
            "tags": ["数据库", "SQL"]
        },
        {
            "name": "search-engine",
            "displayName": "搜索引擎",
            "description": "全文搜索",
            "tags": ["搜索", "引擎"]
        },
        {
            "name": "api-gateway",
            "displayName": "API网关",
            "description": "路由管理",
            "tags": ["API", "网关"]
        },
        {
            "name": "cache-manager",
            "displayName": "缓存管理",
            "description": "Redis/Memcached",
            "tags": ["缓存", "Redis"]
        },
        {
            "name": "json-transformer",
            "displayName": "JSON处理",
            "description": "数据转换",
            "tags": ["JSON", "转换"]
        },
        {
            "name": "csv-exporter",
            "displayName": "CSV导出",
            "description": "报表生成",
            "tags": ["CSV", "导出"]
        },
        {
            "name": "api-documentation",
            "displayName": "API文档",
            "description": "OpenAPI规范",
            "tags": ["API", "文档"]
        },
        {
            "name": "etl-pipeline",
            "displayName": "ETL管道",
            "description": "数据处理",
            "tags": ["ETL", "数据"]
        },
        {
            "name": "query-builder",
            "displayName": "查询构建",
            "description": "条件过滤",
            "tags": ["查询", "构建"]
        },
        {
            "name": "data-validator",
            "displayName": "数据验证",
            "description": "Schema验证",
            "tags": ["验证", "Schema"]
        },
    ],
    
    # ========== 设计与 UI ==========
    "design": [
        {
            "name": "ui-component",
            "displayName": "UI组件",
            "description": "React/Vue组件",
            "tags": ["UI", "组件"]
        },
        {
            "name": "template-engine",
            "displayName": "模板引擎",
            "description": "模板生成",
            "tags": ["模板", "引擎"]
        },
        {
            "name": "responsive-layout",
            "displayName": "响应式布局",
            "description": "适配方案",
            "tags": ["响应式", "布局"]
        },
        {
            "name": "animation-tool",
            "displayName": "动效工具",
            "description": "动画制作",
            "tags": ["动画", "动效"]
        },
        {
            "name": "icon-set",
            "displayName": "图标集",
            "description": "矢量图标",
            "tags": ["图标", "矢量"]
        },
        {
            "name": "color-theme",
            "displayName": "主题配色",
            "description": "配色方案",
            "tags": ["颜色", "主题"]
        },
        {
            "name": "typography-guide",
            "displayName": "字体排版",
            "description": "字体规范",
            "tags": ["字体", "排版"]
        },
    ],
    
    # ========== DevOps ==========
    "devops": [
        {
            "name": "docker-build",
            "displayName": "Docker构建",
            "description": "容器化",
            "tags": ["Docker", "容器"]
        },
        {
            "name": "ci-cd-pipeline",
            "displayName": "CI/CD管道",
            "description": "自动化部署",
            "tags": ["CI/CD", "部署"]
        },
        {
            "name": "serverless-deploy",
            "displayName": "无服务器部署",
            "description": "函数计算",
            "tags": ["Serverless", "函数"]
        },
        {
            "name": "monitoring-stack",
            "displayName": "监控栈",
            "description": "Prometheus/Grafana",
            "tags": ["监控", "Prometheus"]
        },
        {
            "name": "secret-manager",
            "displayName": "密钥管理",
            "description": "环境变量",
            "tags": ["密钥", "Secret"]
        },
        {
            "name": "load-balancer",
            "displayName": "负载均衡",
            "description": "流量分配",
            "tags": ["负载", "均衡"]
        },
        {
            "name": "log-aggregation",
            "displayName": "日志聚合",
            "description": "ELK栈",
            "tags": ["日志", "ELK"]
        },
        {
            "name": "service-mesh",
            "displayName": "服务网格",
            "description": "Istio/Linkerd",
            "tags": ["服务网格", "Mesh"]
        },
    ],
}

def get_all_skills() -> List[Dict]:
    """获取所有 Skills"""
    all_skills = []
    for category, skills in KNOWN_SKILLS.items():
        for skill in skills:
            skill['category'] = category
            all_skills.append(skill)
    return all_skills

def get_skills_by_category(category: str) -> List[Dict]:
    """按分类获取"""
    return KNOWN_SKILLS.get(category, [])

def search_skills(keyword: str) -> List[Dict]:
    """搜索 Skills"""
    keyword = keyword.lower()
    results = []
    for category, skills in KNOWN_SKILLS.items():
        for skill in skills:
            text = f"{skill['displayName']} {skill['description']} {' '.join(skill.get('tags', []))}".lower()
            if keyword in text:
                skill['category'] = category
                results.append(skill)
    return results

def get_stats() -> Dict[str, int]:
    """获取统计"""
    return {cat: len(skills) for cat, skills in KNOWN_SKILLS.items()}

if __name__ == "__main__":
    stats = get_stats()
    total = sum(stats.values())
    print(f"📦 已收录 {total} 个 Skills")
    print(f"📂 分类: {len(stats)} 个")
    for cat, count in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")
