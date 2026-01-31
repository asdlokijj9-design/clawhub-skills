#!/usr/bin/env pwsh
# ClawHub Skills 同步系统 - GitHub 配置脚本

Write-Host "=======================================" -ForegroundColor Cyan
Write-Host "  ClawHub Skills - GitHub 配置" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

# 1. 检查是否安装了 Git
Write-Host "[1/5] 检查 Git 安装..." -ForegroundColor Yellow
try {
    $gitVersion = git --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✅ Git 已安装: $gitVersion" -ForegroundColor Green
    } else {
        Write-Host "  ❌ Git 未安装，请先安装 Git" -ForegroundColor Red
        Write-Host "    下载地址: https://git-scm.com/download/win" -ForegroundColor Gray
        exit 1
    }
} catch {
    Write-Host "  ❌ Git 未安装，请先安装 Git" -ForegroundColor Red
    exit 1
}

# 2. 配置 Git 用户 "[2/5信息
Write-Host] 配置 Git 用户信息..." -ForegroundColor Yellow
git config --global user.name "Moltbot User" 2>&1 | Out-Null
git config --global user.email "asdlokijj9@gmail.com" 2>&1 | Out-Null
Write-Host "  ✅ 已配置用户信息" -ForegroundColor Green

# 3. 创建 .gitignore
Write-Host "[3/5] 创建 .gitignore..." -ForegroundColor Yellow
@"
# 排除文件
*.log
.DS_Store
Thumbs.db
skills_db_backup.json
"@ | Out-File -FilePath ".gitignore" -Encoding utf8
Write-Host "  ✅ 已创建 .gitignore" -ForegroundColor Green

# 4. 初始化 Git 仓库
Write-Host "[4/5] 初始化 Git 仓库..." -ForegroundColor Yellow
if (-not (Test-Path ".git")) {
    git init 2>&1 | Out-Null
    Write-Host "  ✅ Git 仓库已初始化" -ForegroundColor Green
} else {
    Write-Host "  ℹ️  Git 仓库已存在" -ForegroundColor Gray
}

# 5. 提示配置 Token
Write-Host "[5/5] GitHub Token 配置" -ForegroundColor Yellow
Write-Host ""
Write-Host "  ⚠️  请配置 GitHub Token（替代密码，更安全）" -ForegroundColor Yellow
Write-Host ""
Write-Host "  配置方式（选择一种）：" -ForegroundColor White
Write-Host ""
Write-Host "  方式 A - 环境变量（推荐）：" -ForegroundColor Gray
Write-Host "      \$env:GITHUB_TOKEN = 'ghp_你的token'" -ForegroundColor Gray
Write-Host "      并将此行添加到你的 PowerShell 配置文件" -ForegroundColor Gray
Write-Host ""
Write-Host "  方式 B - Credential Manager：" -ForegroundColor Gray
Write-Host "      git config --global credential.helper wincred" -ForegroundColor Gray
Write-Host ""
Write-Host "  方式 C - 手动输入（本次会话有效）：" -ForegroundColor Gray
Write-Host "      输入你的 GitHub Token: " -ForegroundColor Gray -NoNewline
$token = Read-Host
if ($token) {
    $env:GITHUB_TOKEN = $token
    Write-Host "      ✅ Token 已临时保存（重启后失效）" -ForegroundColor Green
}

Write-Host ""
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host "  ✅ GitHub 配置完成！" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  下一步：" -ForegroundColor White
Write-Host "  1. 创建 GitHub 远程仓库" -ForegroundColor Gray
Write-Host "  2. 运行 .\sync.ps1 同步数据" -ForegroundColor Gray
Write-Host ""
