# 💥 第四章：卸载与重装

> 安全撤离，随时能回来

---

## 4.1 什么时候需要卸载？

### 常见场景

【信息框 - 黄色】
⚠️ **以下情况你可能需要卸载 OpenClaw：**

- 🤔 "系统太乱了，想完全重装"（推荐：卸载➜重装➜恢复快照）
- 💻 "换电脑了，要把配置迁到新机器"（推荐：导出快照➜新机器导入）
- 🧹 "磁盘空间不足，想清理一下"（慎用：会丢失配置）
- 🔧 "OpenClaw 出问题了，想彻底重装试试"（推荐：先诊断再决定）
- 🆕 "想升级到新版，但配置太旧"（推荐：升级工具，不用卸载）

---

## 4.2 安全卸载流程

### 4.2.1 启动卸载虾

【代码块 - bash】
```bash
ocu
# 或
openclaw-uninstall
```

### 4.2.2 选择备份方式

卸载虾会提示你选择备份方式：

【代码块 - text】
```
💥 ╔═══════════════════════════════════════╗
  ║     OpenClaw 完全卸载工具             ║
  ║      💾 先存档，再告别 👋             ║
  ╚═══════════════════════════════════════╝

选项:
1. 📦 保存为 tar.gz 文件（推荐，可导出到其他机器）
2. 📁 保存到快照目录（配合 ocs 命令恢复）
3. 🚫 跳过备份（配置将丢失！）

请选择 (1/2/3):
```

### 4.2.3 推荐：选项 1（导出 tar.gz）

【代码块 - text】
```
请选择 (1/2/3): 1
保存路径 [/home/user/Desktop]: /mnt/backup

🦐 正在努力... 🦞 加油加载...

       📸 ✨
      ╱    ╲
     │  💾  │   ← 快照已保存
      ╲    ╱
       ────
   你的身份已安全存档
   重装后可随时恢复！

✅ 快照已保存!
  📦 文件: /mnt/backup/openclaw_backup_20250115_143022.tar.gz
  💾 大小: 12.5 MB
  🔖 校验: a1b2c3d4
```

### 4.2.4 卸载过程

【流程图】
```
开始卸载
    │
    ├── 步骤1: 🛑 停止服务
    │      └── 查找并停止 OpenClaw 进程
    │
    ├── 步骤2: 💾 创建快照
    │      └── 备份 ~/.openclaw 目录
    │
    ├── 步骤3: 📦 卸载 npm 包
    │      └── npm uninstall -g openclaw
    │
    ├── 步骤4: 🗑️ 删除文件
    │      └── 删除 ~/.openclaw 及相关文件
    │
    └── 步骤5: 🧹 清理环境变量
           └── 清理 shell 配置文件

✅ 卸载完成！
```

---

## 4.3 重新安装

### 4.3.1 安装 OpenClaw

【代码块 - bash】
```bash
# 方法1：官方安装脚本
curl -fsSL https://openclaw.ai/install.sh | bash

# 方法2：npm 安装
npm install -g openclaw

# 方法3：部署虾（如需同时配置飞书）
pip install openclaw-feishu-deployer
ofd deploy
```

### 4.3.2 基础配置

【代码块 - bash】
```bash
# 配置 AI 模型
openclaw onboard

# 或编辑配置文件
openclaw config
```

---

## 4.4 恢复配置

### 4.4.1 方法1：使用备份虾恢复快照

【代码块 - bash】
```bash
# 1. 安装备份工具
pip install openclaw-snapshot

# 2. 导入之前导出的快照
ocs import /mnt/backup/openclaw_backup_20250115_143022.tar.gz

# 3. 查看可用快照
ocs list

# 4. 恢复
ocs restore openclaw_backup_20250115_143022

# 5. 重启服务
openclaw gateway restart
```

### 4.4.2 方法2：手动解压恢复

【折叠块：手动恢复步骤】
如果你不想用 ocs 工具，可以手动恢复：

```bash
# 1. 停止服务
openclaw gateway stop

# 2. 解压快照
cd ~
tar -xzf /mnt/backup/openclaw_backup_20250115_143022.tar.gz

# 3. 移动配置到正确位置
rm -rf ~/.openclaw  # 删除新安装的空配置
mv ~/openclaw_backup_20250115_143022/openclaw_data ~/.openclaw

# 4. 重启服务
openclaw gateway restart
```

---

## 4.5 完整重装案例

### 场景：系统重装后恢复 OpenClaw

【折叠块：详细步骤】
**目标：** 原系统崩溃，重装 Ubuntu 后恢复 OpenClaw

**前提：** 之前用 `ocu` 导出了快照到 U 盘

**步骤：**

1. **新系统安装基础环境**
   ```bash
   # 安装 Python 和 Node.js
   sudo apt update
   sudo apt install python3 python3-pip nodejs npm
   
   # 验证
   python3 --version  # 3.7+
   node --version     # 18+
   ```

2. **从 U 盘复制快照**
   ```bash
   cp /media/user/USB/openclaw_backup_xxx.tar.gz ~/Desktop/
   ```

3. **安装 OpenClaw**
   ```bash
   curl -fsSL https://openclaw.ai/install.sh | bash
   ```

4. **安装并恢复快照**
   ```bash
   pip install openclaw-snapshot
   ocs import ~/Desktop/openclaw_backup_xxx.tar.gz
   ocs restore openclaw_backup_xxx
   ```

5. **重启服务**
   ```bash
   openclaw gateway restart
   ```

6. **验证**
   ```bash
   openclaw gateway status
   # 在飞书测试机器人
   ```

**完成！** 所有配置恢复如初 🎉

---

## 4.6 故障排查

### Q: 卸载时提示"进程无法停止"？

【折叠块：解决方案】
```bash
# 强制停止
sudo pkill -9 -f openclaw

# 等待几秒
sleep 3

# 重新运行卸载
ocu
```

### Q: 恢复快延后身份验证失败？

【折叠块：排查】
```bash
# 检查凭证文件权限
ls -la ~/.openclaw/credentials/

# 可能需要重新授权
openclaw config
# 然后重新输入 API Key
```

### Q: 快照导入失败？

【折叠块：解决】
```bash
# 检查文件完整性
tar -tzf openclaw_backup_xxx.tar.gz

# 如果损坏，尝试从其他备份恢复
# 或重新配置
```

---

## 4.7 下一步

【按钮】
→ [第五章：高级使用](链接)

学会卸载和恢复后，探索更高级的玩法：
- 命令行技巧
- 自动化脚本
- 故障诊断

---

*第四章完*

📊 **本章统计**
- 预计阅读时间：10分钟
- 预计操作时间：15分钟（卸载+重装+恢复）
- 难度：⭐⭐（中等，但有保护措施）
