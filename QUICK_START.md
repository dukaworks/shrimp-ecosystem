# 📖 虾族生态快速手册
# Quick Start Guide

> 5分钟上手，30分钟精通

---

## 🎯 一句话介绍

**虾族生态** = 三个可爱工具，帮你轻松管理 OpenClaw

```
🦞 部署虾 (ofd)  →  安装 OpenClaw
💾 备份虾 (ocs)  →  保存配置快照
💥 卸载虾 (ocu)  →  清理并备份
```

---

## ⚡ 5分钟快速开始

### 1. 安装（1分钟）

```bash
pip install openclaw-feishu-deployer openclaw-uninstaller openclaw-snapshot
```

### 2. 部署（3分钟）

```bash
# 启动部署向导
ofd deploy

# 按提示完成：
# 1. 选择 AI 模型
# 2. 配置飞书机器人
# 3. 完成
```

### 3. 备份（1分钟）

```bash
# 保存当前状态
ocs create

# 输入名称: my_first_backup
# 类型选择: 2. 当前状态
```

**完成！** 🎉

---

## 📚 常用命令速查

### 部署虾 (ofd)

```bash
ofd deploy              # 部署向导
ofd --help              # 查看帮助
```

### 备份虾 (ocs)

```bash
ocs create              # 创建快照
ocs list                # 列出快照
ocs restore <ID>        # 恢复快照
ocs export <ID>         # 导出快照
ocs import <file>       # 导入快照
ocs delete <ID>         # 删除快照
ocs fresh               # 快速创建纯净快照
```

### 卸载虾 (ocu)

```bash
ocu                     # 交互式卸载
ocu -y                  # 自动确认（危险）
```

---

## 🔄 典型工作流

### 工作流1：新用户部署

```
安装 → 部署 → 备份

1. pip install ...
2. ofd deploy
3. ocs fresh  (创建纯净快照)
```

### 工作流2：日常维护

```
定期备份 → 需要时恢复

每周运行: ocs create
名称: weekly_YYYYMMDD
类型: 当前状态

恢复时: ocs restore <ID>
```

### 工作流3：重装系统

```
卸载备份 → 重装 → 恢复

1. ocu
   选择: 📦 保存为 tar.gz
   路径: ~/Desktop/

2. 重新安装系统

3. 重新安装 OpenClaw

4. ocs import ~/Desktop/backup.tar.gz
   ocs restore <ID>
```

### 工作流4：迁移到新机器

```
旧机器导出 → 新机器导入

旧机器:
1. ocs export my_config
2. scp my_config.tar.gz new-machine:~/

新机器:
1. 安装 OpenClaw
2. ocs import ~/my_config.tar.gz
3. ocs restore my_config
```

---

## 🆘 常见问题

### Q: 部署失败？

```bash
# 检查环境
python3 --version    # 需要 3.7+
node --version       # 需要 18+

# 查看日志
openclaw gateway logs

# 诊断问题
openclaw doctor
```

### Q: 快照太大？

```bash
# 清理日志和缓存
rm -rf ~/.openclaw/logs/
rm -rf ~/.openclaw/media/

# 重新创建快照
ocs create
```

### Q: 恢复快照失败？

```bash
# 停止服务
openclaw gateway stop

# 手动恢复
tar -xzf backup.tar.gz -C ~
mv ~/openclaw_backup_*/openclaw_data ~/.openclaw

# 重启
openclaw gateway start
```

### Q: 忘记快照ID？

```bash
ocs list
# 查看所有快照，按时间排序
```

---

## 💡 最佳实践

### ✅ 应该做的

1. **部署后立即创建纯净快照**
   ```bash
   ofd deploy
   ocs fresh
   ```

2. **定期备份（建议每周）**
   ```bash
   # 添加到 crontab
   0 2 * * 0 ocs create <<< "weekly_$(date +\%Y\%m\%d)"
   ```

3. **重要变更前备份**
   ```bash
   ocs create
   # 然后大胆尝试新配置
   ```

4. **导出快照到外部存储**
   ```bash
   ocs export my_config
   # 复制到 U 盘 / 云盘
   ```

### ❌ 不应该做的

1. ~~从不备份~~
2. ~~卸载前不创建快照~~
3. ~~所有配置混在一起~~
4. ~~忘记快照保存在哪里~~

---

## 📁 文件位置

```
~/.openclaw/                    # OpenClaw 主目录
~/.openclaw_snapshots/          # 快照存储
~/.openclaw_backup/             # 自动备份
~/Desktop/openclaw_backup_*.tar.gz  # 导出的快照
```

---

## 🔗 相关链接

- **GitHub**: https://github.com/dukaworks
  - [openclaw-feishu-deployer](https://github.com/dukaworks/openclaw-feishu-deployer)
  - [openclaw-uninstaller](https://github.com/dukaworks/openclaw-uninstaller)
  - [openclaw-snapshot](https://github.com/dukaworks/openclaw-snapshot)

- **PyPI**:
  - `pip install openclaw-feishu-deployer`
  - `pip install openclaw-uninstaller`
  - `pip install openclaw-snapshot`

- **文档**: （飞书文档链接待添加）

- **社区**: （飞书群二维码待添加）

---

## 🎓 进阶学习

| 主题 | 文档 | 预计时间 |
|------|------|----------|
| 完整部署 | 部署指南 | 30分钟 |
| 备份策略 | 备份指南 | 20分钟 |
| 故障排查 | 故障指南 | 15分钟 |
| 自动化 | 高级使用 | 30分钟 |

---

## 🤝 获取帮助

1. **查看文档** - 本文档和详细指南
2. **GitHub Issues** - 提交问题
3. **飞书群** - 社区讨论
4. **邮件** - chenzhy.bj@gmail.com

---

*快速手册 v1.0 - 虾族生态*  
*建议打印或保存书签*
