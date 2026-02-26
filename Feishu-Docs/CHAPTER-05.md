# 🛠️ 第五章：高级使用

> 从用户到专家，掌握更多技巧

---

## 5.1 命令速查表

### 5.1.1 部署虾 (ofd)

【表格】
| 命令 | 功能 | 示例 |
|------|------|------|
| `ofd deploy` | 启动部署向导 | `ofd deploy` |
| `ofd --version` | 查看版本 | `ofd --version` |
| `ofd --help` | 查看帮助 | `ofd --help` |

### 5.1.2 备份虾 (ocs)

【表格】
| 命令 | 功能 | 示例 |
|------|------|------|
| `ocs create` | 创建快照 | `ocs create` |
| `ocs fresh` | 快速创建纯净快照 | `ocs fresh` |
| `ocs list` | 列出快照 | `ocs list` |
| `ocs restore <ID>` | 恢复快照 | `ocs restore backup_001` |
| `ocs export <ID>` | 导出快照 | `ocs export backup_001` |
| `ocs import <file>` | 导入快照 | `ocs import backup.tar.gz` |
| `ocs delete <ID>` | 删除快照 | `ocs delete old_backup` |

### 5.1.3 卸载虾 (ocu)

【表格】
| 命令 | 功能 | 示例 |
|------|------|------|
| `ocu` | 交互式卸载 | `ocu` |
| `openclaw-uninstall` | 同上 | `openclaw-uninstall` |

### 5.1.4 OpenClaw 自带命令

【表格】
| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw status` | 查看状态 | `openclaw status` |
| `openclaw gateway start` | 启动服务 | `openclaw gateway start` |
| `openclaw gateway stop` | 停止服务 | `openclaw gateway stop` |
| `openclaw gateway restart` | 重启服务 | `openclaw gateway restart` |
| `openclaw gateway logs` | 查看日志 | `openclaw gateway logs` |
| `openclaw config` | 编辑配置 | `openclaw config` |
| `openclaw doctor` | 诊断问题 | `openclaw doctor` |
| `openclaw update status` | 检查更新 | `openclaw update status` |

---

## 5.2 自动化脚本

### 5.2.1 每周自动备份

【代码块 - bash】
```bash
#!/bin/bash
# weekly_backup.sh - 每周自动备份 OpenClaw

# 设置日志
LOG_FILE="$HOME/.openclaw_snapshots/auto_backup.log"
echo "[$(date)] 开始自动备份" >> $LOG_FILE

# 创建带时间戳的快照
BACKUP_NAME="weekly_$(date +%Y%m%d)"

# 使用 ocs 创建快照
echo "$BACKUP_NAME" | ocs create >> $LOG_FILE 2>&1

# 保留最近 4 个周备份，删除旧的
cd ~/.openclaw_snapshots
ls -t | grep '^weekly_' | tail -n +5 | xargs rm -rf

echo "[$(date)] 备份完成: $BACKUP_NAME" >> $LOG_FILE
```

【信息框 - 蓝色】
📌 **添加到 crontab：**
```bash
# 编辑 crontab
crontab -e

# 添加以下行（每周日凌晨2点执行）
0 2 * * 0 /path/to/weekly_backup.sh
```

---

## 5.3 故障排查

### 5.3.1 诊断清单

【检查清单】
- [ ] **服务状态** - `openclaw gateway status`
- [ ] **进程运行** - `pgrep -f openclaw`
- [ ] **端口占用** - `lsof -i :18789`
- [ ] **日志查看** - `openclaw gateway logs | tail -50`
- [ ] **磁盘空间** - `df -h ~/.openclaw`
- [ ] **配置文件** - `cat ~/.openclaw/openclaw.json | jq .`

### 5.3.2 常见问题速查

【折叠块：Gateway 启动失败】
```bash
# 1. 查看详细错误
openclaw gateway logs

# 2. 检查端口占用
lsof -i :18789

# 3. 检查配置文件
openclaw config validate
```

【折叠块：飞书机器人无响应】
```bash
# 1. 检查服务状态
openclaw gateway status

# 2. 检查日志
openclaw gateway logs | grep -i feishu

# 3. 重启试试
openclaw gateway restart
```

---

## 5.4 下一步

→ [第六章：社区与支持](链接)

---

*第五章完*
