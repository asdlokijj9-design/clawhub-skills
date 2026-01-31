#!/usr/bin/env pwsh
# ClawHub Skills 每日同步脚本
# 每天 10:00 自动执行

param(
    [switch]$ForceFetch = $false,  # 强制重新抓取
    [switch]$ManualMode = $false   # 手动模式（无浏览器时使用）
)

$ErrorActionPreference = "Stop"

# 配置
$SKILLS_DIR = "D:\moltbot开发项目\06_待优化方案\clawhub_skills"
$CLAWHUB_URL = "https://www.clawhub.ai/skills"
$DB_FILE = Join-Path $SKILLS_DIR "skills_db.json"
$README_FILE = Join-Path $SKILLS_DIR "README.md"
$CHANGELOG_FILE = Join-Path $SKILLS_DIR "CHANGELOG.md"
$RAW_HTML_FILE = Join-Path $SKILLS_DIR "clawhub_raw.html"

# 功能分类
$CATEGORY_MAP = @{
    "voice"      = "🎙️ 语音相关"
    "browser"    = "🌐 浏览器相关"
    "memory"     = "🧠 记忆相关"
    "message"    = "💬 消息相关"
    "file"       = "📁 文件相关"
    "developer"  = "👨‍💻 开发相关"
    "image"      = "🖼️ 图片相关"
    "calendar"   = "📅 日历相关"
    "ecommerce"  = "🛒 电商相关"
    "ai"         = "🤖 AI 相关"
    "other"      = "📦 其他"
}

Write-Host "=======================================" -ForegroundColor Cyan
Write-Host "  🔄 ClawHub Skills 每日同步" -ForegroundColor Cyan
Write-Host "  $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Gray
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

# 步骤 1: 抓取网站
Write-Host "[1/5] 📡 抓取 ClawHub..." -ForegroundColor Yellow

if ($ManualMode -or $ForceFetch) {
    # 手动模式：直接使用 curl
    Write-Host "  📋 使用手动模式（curl）..." -ForegroundColor Gray
    
    try {
        $response = Invoke-WebRequest -Uri $CLAWHUB_URL -UseBasicParsing -TimeoutSec 15
        $response.Content | Out-File -FilePath $RAW_HTML_FILE -Encoding utf8
        Write-Host "  ✅ HTML 已保存" -ForegroundColor Green
    } catch {
        Write-Host "  ⚠️ 抓取失败: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "  💡 提示: 尝试手动访问 $CLAWHUB_URL" -ForegroundColor Gray
    }
} else {
    # 自动模式：尝试多种方式
    $fetchSuccess = $false
    
    # 方式 1: 尝试 curl
    try {
        $html = curl -s $CLAWHUB_URL 2>&1
        if ($html.Length -gt 100) {
            $html | Out-File -FilePath $RAW_HTML_FILE -Encoding utf8
            $fetchSuccess = $true
            Write-Host "  ✅ curl 成功" -ForegroundColor Green
        }
    } catch {
        Write-Host "  ⚠️ curl 失败" -ForegroundColor Gray
    }
    
    # 方式 2: 尝试 PowerShell Invoke-WebRequest
    if (-not $fetchSuccess) {
        try {
            $response = Invoke-WebRequest -Uri $CLAWHUB_URL -UseBasicParsing -TimeoutSec 15
            if ($response.Content.Length -gt 100) {
                $response.Content | Out-File -FilePath $RAW_HTML_FILE -Encoding utf8
                $fetchSuccess = $true
                Write-Host "  ✅ Invoke-WebRequest 成功" -ForegroundColor Green
            }
        } catch {
            Write-Host "  ⚠️ Invoke-WebRequest 失败" -ForegroundColor Gray
        }
    }
    
    if (-not $fetchSuccess) {
        Write-Host "  ⚠️ 无法自动抓取，切换到手动模式..." -ForegroundColor Yellow
        Write-Host "  💡 请手动访问 $CLAWHUB_URL 并检查是否有新 Skills" -ForegroundColor Gray
    }
}

# 步骤 2: 解析 Skills
Write-Host ""
Write-Host "[2/5] 🔍 解析 Skills..." -ForegroundColor Yellow

$newSkills = @()

# 读取 HTML（如果存在）
if (Test-Path $RAW_HTML_FILE) {
    $html = Get-Content -Path $RAW_HTML_FILE -Raw -Encoding utf8
    Write-Host "  📄  HTML 长度: $($html.Length) 字符" -ForegroundColor Gray
    
    # 由于页面是 SPA，HTML 可能不包含完整数据
    # 这里提供占位符，实际使用需要 Playwright
    Write-Host "  ⚠️  注意: 页面使用 JavaScript 动态加载" -ForegroundColor Yellow
    Write-Host "  💡 需要 Playwright 才能完整解析" -ForegroundColor Gray
    
    # 添加占位示例（实际使用时请删除）
    $newSkills += @{
        name        = "新增 Skill（待确认）"
        description = "请访问 $CLAWHUB_URL 查看最新 Skills"
        url         = $CLAWHUB_URL
        category    = "other"
        fetched_at  = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
    }
} else {
    Write-Host "  ⚠️  未找到 HTML 文件" -ForegroundColor Red
}

# 步骤 3: 更新数据库
Write-Host ""
Write-Host "[3/5] 💾 更新数据库..." -ForegroundColor Yellow

# 加载或创建数据库
if (Test-Path $DB_FILE) {
    $db = Get-Content -Path $DB_FILE -Raw -Encoding utf8 | ConvertFrom-Json
} else {
    $db = @{ skills = @(); last_sync = $null }
}

$beforeCount = $db.skills.Count
$addedCount = 0

# 添加新 Skills
foreach ($skill in $newSkills) {
    # 检查是否已存在
    $exists = $false
    foreach ($existing in $db.skills) {
        if ($existing.url -eq $skill.url) {
            $exists = $true
            break
        }
    }
    
    if (-not $exists) {
        $db.skills += $skill
        $addedCount++
        Write-Host "  ✅ 新增: $($skill.name)" -ForegroundColor Green
    }
}

$db.last_sync = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$db | ConvertTo-Json -Depth 10 | Out-File -FilePath $DB_FILE -Encoding utf8

Write-Host "  📊 数据库统计: $($db.skills.Count) 个 Skills ($addedCount 新增)" -ForegroundColor Gray

# 步骤 4: 生成分类清单
Write-Host ""
Write-Host "[4/5] 📝 生成分类清单..." -ForegroundColor Yellow

# 统计分类
$categoryStats = @{}
foreach ($skill in $db.skills) {
    $cat = $skill.category
    if (-not $cat) { $cat = "other" }
    $categoryStats[$cat] = ($categoryStats[$cat] ?? 0) + 1
}

# 生成 README
$readme = @"
# ClawHub Skills 同步仓库

**最后同步:** $($db.last_sync)  
**数据来源:** [ClawHub](https://www.clawhub.ai/skills)

---

## 📊 统计概览

| 分类 | 数量 |
|------|------|
"@

foreach ($cat in ($categoryStats.Keys | Sort-Object)) {
    $catName = $CATEGORY_MAP[$cat] ?? $cat
    $count = $categoryStats[$cat]
    $readme += "| $catName | $count |`n"
}

$total = ($categoryStats.Values | Measure-Object -Sum).Sum
$readme += "| **总计** | **$total** |`n"

$readme += @"

---

## 📦 分类详情

"@

foreach ($cat in ($categoryStats.Keys | Sort-Object)) {
    $catName = $CATEGORY_MAP[$cat] ?? $cat
    $readme += "### $catName`n`n"
    
    foreach ($skill in $db.skills) {
        if ($skill.category -eq $cat) {
            $desc = if ($skill.description.Length -gt 100) { $skill.description.Substring(0,100) + "..." } else { $skill.description }
            $readme += "- **$($skill.name)** - $desc`n"
        }
    }
    $readme += "`n"
}

$readme | Out-File -FilePath $README_FILE -Encoding utf8
Write-Host "  ✅ 已更新: README.md" -ForegroundColor Green

# 步骤 5: Git 同步
Write-Host ""
Write-Host "[5/5] 🔀 Git 同步..." -ForegroundColor Yellow

# 检查 Token
if (-not $env:GITHUB_TOKEN) {
    Write-Host "  ⚠️  GitHub Token 未配置" -ForegroundColor Yellow
    Write-Host "  💡 运行 .\setup_github.ps1 配置" -ForegroundColor Gray
} else {
    # 初始化（如果需要）
    if (-not (Test-Path ".git")) {
        git init 2>&1 | Out-Null
        Write-Host "  ✅ Git 仓库已初始化" -ForegroundColor Green
    }
    
    # 添加文件
    git add -A 2>&1 | Out-Null
    
    # 提交
    $commitMsg = "Sync: $($db.skills.Count) skills, $($addedCount) new ($(Get-Date -Format 'yyyy-MM-dd'))"
    git commit -m $commitMsg 2>&1 | Out-Null
    
    Write-Host "  ✅ 已提交: $commitMsg" -ForegroundColor Green
}

# 结束
Write-Host ""
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host "  ✅ 同步完成！" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  📁 文件位置:" -ForegroundColor White
Write-Host "  - 数据库: $DB_FILE" -ForegroundColor Gray
Write-Host "  - 分类清单: $README_FILE" -ForegroundColor Gray
Write-Host ""

if ($addedCount -gt 0) {
    Write-Host "  🆕 今日新增: $addedCount 个 Skills" -ForegroundColor Green
} else {
    Write-Host "  ℹ️  今日无新增 Skills" -ForegroundColor Gray
}
