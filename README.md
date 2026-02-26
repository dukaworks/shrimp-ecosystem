# 🦞 虾族生态 Shrimp Clan Ecosystem

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)

> **"养虾千日，用虾一时"**  
> 最专业、最可爱、最完整的 OpenClaw 工具生态

<p align="center">
  <img src="assets/logo.png" alt="虾族生态" width="200">
</p>

---

## 🎯 什么是虾族生态？

**虾族生态**是一套围绕 OpenClaw 构建的专业工具集，提供从部署、使用、备份到卸载的全生命周期管理。

### 核心理念

```
🔄 闭环生态
部署 → 使用 → 备份 → 升级/迁移 → 恢复 → 重新部署
     ↑___________________________________________|

🛡️ 安全第一
任何操作都可逆，任何配置都可备份

🎨 体验至上
可爱的 CLI 界面，让技术工作也有温度
```

---

## 🦞 三叉戟工具集

| 工具 | 图标 | 功能 | 安装 | 命令 |
|------|------|------|------|------|
| **部署虾** | 🦞 | OpenClaw + 飞书一键部署 | `pip install openclaw-feishu-deployer` | `ofd` |
| **卸载虾** | 💥 | 完全卸载 + 自动快照 | `pip install openclaw-uninstaller` | `ocu` |
| **备份虾** | 💾 | 智能快照管理 | `pip install openclaw-snapshot` | `ocs` |

### 一键安装所有工具

```bash
pip install openclaw-feishu-deployer openclaw-uninstaller openclaw-snapshot
```

---

## ⚡ 5分钟快速开始

### 1. 部署 OpenClaw

```bash
# 启动部署向导
ofd deploy

# 按提示完成配置
```

### 2. 创建初始快照

```bash
# 保存纯净安装状态
ocs fresh
```

### 3. 日常使用

```bash
# 定期备份
ocs create

# 查看快照
ocs list

# 需要时恢复
ocs restore <快照ID>
```

### 4. 安全卸载（如需要）

```bash
# 卸载前自动创建快照
ocu
```

---

## 📚 文档导航

### 必读文档

| 文档 | 内容 | 阅读时间 |
|------|------|----------|
| [QUICK_START.md](QUICK_START.md) | 5分钟快速上手指南 | 5分钟 |
| [ECOSYSTEM.md](ECOSYSTEM.md) | 完整生态介绍与架构 | 15分钟 |
| [FEISHU_DOCS_PLAN.md](FEISHU_DOCS_PLAN.md) | 飞书文档制作方案 | 10分钟 |
| [ROADMAP.md](ROADMAP.md) | 未来发展路线图 | 10分钟 |

### 详细指南

- **部署指南** - 完整的 OpenClaw + 飞书部署教程
- **备份指南** - 快照管理与跨机迁移
- **卸载与恢复** - 安全卸载与配置恢复
- **故障排查** - 常见问题与解决方案

> 📖 详细指南请在飞书文档中查看（链接待添加）

---

## 🎨 特色功能

### 💾 智能快照

- **纯净快照** - 刚装好的状态
- **当前快照** - 完整配置备份
- **自动快照** - 卸载前自动备份
- **导出/导入** - 跨机器迁移

### 🛡️ 安全保护

- **二次确认** - 危险操作需确认
- **自动备份** - 卸载前自动存档
- **恢复指南** - 详细的恢复步骤
- **校验和** - 确保快照完整性

### 🎭 可爱界面

```
🦞 ╔═══════════════════════════════════════╗
  ║     OpenClaw + Feishu 部署小助手      ║
  ╚═══════════════════════════════════════╝

[████░░░░░░░░░░░] 步骤 1/7
📝 检查环境准备情况 🔍

✅ Node.js 已安装
🦐 正在努力... 🦞 加油加载...
```

---

## 🔮 未来规划

### Phase 2: 六虾战队 (进行中)

- 🏥 **健康虾** - 诊断与监控
- ⬆️ **升级虾** - 版本升级管理
- ⚙️ **配置虾** - 配置管理

### Phase 3: 可视化平台

- Web 管理仪表盘
- 移动端 App

### Phase 4: 生态平台

- 插件市场
- 云服务
- 企业版

查看详细路线图：[ROADMAP.md](ROADMAP.md)

---

## 🤝 加入我们

虾族生态是开源项目，欢迎贡献！

### 如何贡献

1. **提交 Issue** - 报告 Bug 或提出功能建议
2. **提交 PR** - 改进代码或文档
3. **分享经验** - 帮助其他用户
4. **宣传推广** - 让更多人知道虾族生态

### 联系方式

- **GitHub**: https://github.com/dukaworks
- **Email**: chenzhy.bj@gmail.com
- **飞书**: （群二维码待添加）

---

## 📦 项目仓库

| 项目 | 仓库 | PyPI |
|------|------|------|
| 部署虾 | [openclaw-feishu-deployer](https://github.com/dukaworks/openclaw-feishu-deployer) | `pip install openclaw-feishu-deployer` |
| 卸载虾 | [openclaw-uninstaller](https://github.com/dukaworks/openclaw-uninstaller) | `pip install openclaw-uninstaller` |
| 备份虾 | [openclaw-snapshot](https://github.com/dukaworks/openclaw-snapshot) | `pip install openclaw-snapshot` |

---

## 📄 许可证

MIT License © 2025 Duka Works

---

<p align="center">
  🦞 <strong>Made with love by 虾族</strong> 🦞
  <br>
  部署虾 · 卸载虾 · 备份虾 · 健康虾(coming) · 升级虾(coming) · 配置虾(coming)
</p>
