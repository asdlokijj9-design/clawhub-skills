# 🦞 ClawHub Skills 完整分类列表

> 总 Skills: **65个** | 分类: **15个**

---

## 📊 统计概览

| 分类 | 数量 |
|------|------|
| 图像与视频 | 11 |
| 开发者工具 | 9 |
| 通信与消息 | 7 |
| 语音与音频 | 7 |
| 笔记与知识管理 | 6 |
| 文件与系统 | 5 |
| 任务管理与日历 | 4 |
| 浏览器与网络 | 3 |
| 节点与硬件控制 | 3 |
| 智能家居 | 2 |
| 地图与位置 | 2 |
| 食物与外卖 | 2 |
| 监控与通知 | 2 |
| 社交媒体 | 1 |
| 工具与实用工具 | 1 |

---

## 分类详情

### 🖼️ 图像与视频 (11)
- **BluOS 控制**: BluOS CLI (blu)，用于发现、播放、分组和音量控制
- **GIF 搜索**: 使用 CLI/TUI 搜索 GIF 提供商，下载结果，提取静态图或拼贴图
- **Gemini 图像生成**: 通过 Gemini 3 Pro Image 生成或编辑图像（Nano Banana Pro）
- **OpenAI 图像生成**: 通过 OpenAI Images API 批量生成图像，包含随机提示词采样器和 HTML 查看器
- **PDF 编辑**: 使用自然语言指令通过 nano-pdf CLI 编辑 PDF
- **Sonos 控制**: 控制 Sonos 扬声器（发现/状态/播放/音量/分组）
- **Spotify 播放**: 终端 Spotify 播放/搜索，通过 spogo（首选）或 spotify_player
- **图像分析**: 使用配置的图像模型分析图像内容
- **摄像头捕获**: 从 RTSP/ONVIF 摄像头捕获帧或片段
- **视频帧提取**: 使用 ffmpeg 从视频中提取帧或短片段
- **频谱分析**: 通过 songs CLI 从音频生成频谱图和特征面板可视化

### 👨‍💻 开发者工具 (9)
- **Gemini CLI**: Gemini CLI 用于一次性问答、摘要和生成
- **GitHub 操作**: 使用 gh CLI 与 GitHub 交互，使用 gh issue、gh pr、gh run 等命令
- **MCP 客户端**: 使用 mcporter CLI 列出、配置、认证和直接调用 MCP 服务器/工具
- **Oracle CLI**: 使用 oracle CLI 的最佳实践（提示+文件打包、引擎、会话管理）
- **Skill 创建器**: 创建或更新 AgentSkills，用于设计、组织或打包 skills
- **Tmux 控制**: 远程控制 tmux 会序，通过发送按键和截图交互式 CLI
- **文本摘要**: 从 URL、播客和本地文件摘要或提取文本/转录（great for lectures）
- **模型使用统计**: 使用 CodexBar CLI 本地成本使用情况，汇总 Codex 或 Claude 的每模型使用情况
- **编码代理**: 通过后台进程运行 Codex CLI、Claude Code、OpenCode 或 Pi Coding Agent

### 💬 通信与消息 (7)
- **BlueBubbles 消息**: 构建或更新 BlueBubbles 外部频道插件，支持 REST API 和 Webhook
- **Discord 控制**: 通过 discord 工具控制 Discord，发送消息、管理频道
- **Google Workspace**: Google Workspace CLI，用于 Gmail、日历、云端硬盘、联系人、表格和文档
- **Slack 控制**: 通过 slack 工具控制 Slack，发送消息、管理频道
- **WhatsApp 消息**: 发送 WhatsApp 消息给其他人，搜索/同步 WhatsApp 历史
- **iMessage 消息**: iMessage/SMS CLI，用于列出聊天、查看历史、监听和发送消息
- **邮件管理**: 通过 IMAP/SMTP 管理邮件，使用 himalaya 列出、读取、编写、回复邮件

### 🎙️ 语音与音频 (7)
- **API 语音识别**: 通过 OpenAI Audio Transcriptions API (Whisper) 转录音频
- **ElevenLabs TTS**: ElevenLabs 文本转语音，带 mac 风格 say UX
- **文字转语音 (TTS)**: 将文本转换为语音并返回 MEDIA 路径
- **本地 TTS**: 通过 sherpa-onnx 进行本地文本转语音（离线，无需云服务）
- **本地语音识别**: 使用 Whisper CLI 进行本地语音转文本（无需 API key）
- **语音唤醒**: 语音唤醒词检测，支持自定义关键词
- **语音通话**: 通过 OpenClaw voice-call 插件启动语音通话

### 📝 笔记与知识管理 (6)
- **Apple Notes**: 在 macOS 上通过 memo CLI 管理 Apple Notes（创建、查看、编辑、删除、搜索）
- **Bear 笔记**: 通过 grizzly CLI 创建、搜索和管理 Bear 笔记
- **Notion 协作**: Notion API，用于创建和管理页面、数据库和块
- **Obsidian 笔记**: 使用 Obsidian vaults（纯 Markdown 笔记），通过 obsidian-cli 自动化
- **会话日志分析**: 使用 jq 搜索和分析自己的会话日志（旧对话/父对话）
- **记忆管理**: 语义搜索和读取记忆文件（MEMORY.md, memory/*.md）

### ⚙️ 文件与系统 (5)
- **1Password CLI**: 设置和使用 1Password CLI (op)，用于安装 CLI、启用桌面应用集成
- **Gateway 管理**: 重启、配置或更新 Gateway 服务
- **Shell 命令执行**: 执行 Shell 命令，支持 PTY、后台运行和超时控制
- **macOS UI 自动化**: 使用 Peekaboo CLI 捕获和自动化 macOS UI
- **文件操作**: 读取、写入、编辑文件内容

### ✅ 任务管理与日历 (4)
- **Apple 提醒事项**: 在 macOS 上通过 remindctl CLI 管理 Apple 提醒事项（列出、添加、编辑、完成）
- **Things 3 管理**: 在 macOS 上通过 things CLI 管理 Things 3（通过 URL 添加/更新项目和待办）
- **Trello 管理**: 通过 Trello REST API 管理 Trello 看板、列表和卡片
- **定时任务调度**: 管理 Gateway 定时任务和唤醒事件

### 🌐 浏览器与网络 (3)
- **浏览器控制**: 通过 OpenClaw 浏览器控制服务控制浏览器（导航、点击、截图等）
- **网络搜索**: 使用 Brave Search API 进行网络搜索
- **网页内容抓取**: 从 URL 获取并提取可读内容（HTML 转 Markdown/文本）

### 🔌 节点与硬件控制 (3)
- **画布控制**: 控制节点画布（呈现/隐藏/截图/A2UI）
- **节点控制**: 发现和控制配对节点（状态/描述/相机/屏幕/位置/运行）
- **语音通话**: 通过 OpenClaw voice-call 插件启动语音通话

### 🏠 智能家居 (2)
- **Eight Sleep 控制**: 控制 Eight Sleep pods（状态、温度、闹钟、 schedules）
- **Philips Hue 控制**: 通过 OpenHue CLI 控制 Philips Hue 灯光和场景

### 📍 地图与位置 (2)
- **Google Places 搜索**: 通过 goplaces CLI 使用 Google Places API (New) 进行文本搜索和地点详情查询

### 🍔 食物与外卖 (2)
- **Foodora**: 食品/外卖相关

### 📊 监控与通知 (2)
- **博客监控**: 监控博客更新
- **天气**: 天气信息

### 🐦 社交媒体 (1)
- **X/Twitter**: Twitter 相关功能

### 🛠️ 实用工具 (1)
- **ClawdHub**: ClawHub 工具

---

## 🎯 核心亮点

✅ 每个技能都有详细描述-知道具体能做什么  
✅ 点击功能分类领域-快速找到需要的工具  
✅ 附加平台兼容性-跨平台与 macOS 专用  
✅ 飞书通知-每天10:00自动同步  
✅ GitHub 仓库-完整备份和历史追踪

---

*💡 提示: 通过 OpenClaw 集成的工具可以直接使用这些 Skills*
