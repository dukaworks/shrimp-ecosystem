# 🚀 第二章：部署指南

> 从零开始，5分钟部署 OpenClaw + 飞书机器人

---

## 2.1 环境准备检查清单

在开始前，请确认以下环境已准备好：

【检查清单】
- [ ] **Python 3.7+**
  ```bash
  python3 --version  # 应显示 3.7 或更高
  ```
  【折叠块：安装 Python】
  **macOS:**
  ```bash
  brew install python
  ```
  
  **Ubuntu/Debian:**
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```
  
  **Windows:**
  从 [python.org](https://python.org) 下载安装包

- [ ] **Node.js 18+**
  ```bash
  node --version  # 应显示 v18 或更高
  ```
  【折叠块：安装 Node.js】
  **使用 nvm（推荐）:**
  ```bash
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
  nvm install 20
  nvm use 20
  ```

- [ ] **飞书管理员权限**
  - 需要能创建企业自建应用
  - 如果没有，联系你们公司的飞书管理员

- [ ] **AI 模型 API Key**
  - 推荐：Kimi / DeepSeek / Gemini
  - 备选：OpenAI / Claude / Azure

【信息框 - 绿色】
✅ 如果以上都准备好了，让我们开始吧！

---

## 2.2 安装部署工具

### 2.2.1 一键安装三叉戟

【代码块 - bash】
```bash
pip install openclaw-feishu-deployer openclaw-uninstaller openclaw-snapshot
```

【信息框 - 蓝色】
📌 这会同时安装三个工具：
- `ofd` - 部署虾
- `ocu` - 卸载虾
- `ocs` - 备份虾

### 2.2.2 验证安装

【代码块 - bash】
```bash
ofd --version
```

应该显示版本号，例如：`openclaw-feishu-deployer 1.0.0`

如果显示 `command not found`，尝试：

【折叠块：解决命令找不到】
```bash
# 方法1：使用 Python 模块方式
python3 -m openclaw_feishu_deployer --version

# 方法2：检查 pip 安装路径
which pip
# 确保 pip 对应的 Python 在 PATH 中

# 方法3：重新安装
pip install --user openclaw-feishu-deployer
```

---

## 2.3 运行部署向导

### 2.3.1 启动部署

【代码块 - bash】
```bash
ofd deploy
```

你会看到可爱的 CLI 界面：

【代码块 - text】
```
    🦞 ╔═══════════════════════════════════════╗
      ║     OpenClaw + Feishu 部署小助手      ║
      ║        让 AI 助手飞入你的飞书          ║
      ╚═══════════════════════════════════════╝

你好！我是你的 OpenClaw + 飞书部署小助手 🦞
我会一步步带你完成部署~

[░░░░░░░░░░░░░░░] 步骤 1/7
📝 检查环境准备情况 🔍
```

### 2.3.2 部署流程

【流程图】
```
开始
  │
  ├── 步骤1: 检查环境 ─── 检查 Python、Node.js
  │
  ├── 步骤2: 安装 OpenClaw ─── npm install
  │
  ├── 步骤3: 配置 OpenClaw ─── 选择模型、输入 API Key
  │
  ├── 步骤4: 启动 Gateway ─── openclaw gateway start
  │
  ├── 步骤5: 收集飞书凭证 ─── App ID、App Secret
  │
  ├── 步骤6: 对接配置 ─── 连接飞书与 OpenClaw
  │
  └── 步骤7: 重启验证 ─── 测试机器人
       │
       ▼
    完成！🎉
```

### 2.3.3 关键步骤详解

#### 步骤3: 配置 AI 模型

【信息框 - 蓝色】
📌 需要选择 LLM 提供商并输入 API Key

推荐选择（国内可用）：
- **Kimi** (Moonshot) - 推荐，性价比高
- **DeepSeek** - 推理能力强
- **智谱 GLM** - 中文效果好

国际选项：
- **OpenAI GPT** - 能力强但需翻墙
- **Claude** - 安全合规
- **Gemini** - Google 出品

#### 步骤5: 飞书配置

【信息框 - 黄色】
⚠️ 此时需要暂停，去飞书开放平台创建应用

具体步骤见 2.4 节

---

## 2.4 飞书机器人配置

### 2.4.1 创建飞书应用

【折叠块：详细步骤（带截图）】
1. 访问 [飞书开放平台](https://open.feishu.cn)
2. 登录开发者后台
3. 点击「创建企业自建应用」
4. 填写信息：
   - 应用名称：例如「AI助手」或「OpenClaw」
   - 应用描述：智能助手
   - 上传应用图标（可选）

【图片 - 创建应用截图】

### 2.4.2 获取凭证

创建完成后：

1. 进入「凭据管理」页面
2. 复制 **App ID** 和 **App Secret**
3. 保存好，后面会用到

【图片 - 凭据管理页面截图】

【信息框 - 红色】
❗ **App Secret 只显示一次！** 请立即复制保存

### 2.4.3 开通权限

进入「权限管理」：

【代码块 - json】
```json
{
  "permissions": [
    "im:message:send",
    "im:message:receive", 
    "im:chat:readonly",
    "contact:user.base:readonly"
  ]
}
```

点击「批量导入」，粘贴以上 JSON，然后申请开通。

### 2.4.4 配置事件订阅

进入「事件与回调」：

1. 订阅方式：选择「使用长连接接收事件」
2. 添加事件：勾选「接收消息」等消息类事件
3. 保存

【图片 - 事件订阅配置截图】

### 2.4.5 发布应用

进入「版本管理与发布」：

1. 点击「创建版本」
2. 版本号：`1.0.0`
3. 更新说明：`初始版本`
4. 申请发布
5. 在飞书客户端审批通过

【图片 - 版本发布截图】

---

## 2.5 验证部署

### 2.5.1 检查服务状态

【代码块 - bash】
```bash
openclaw gateway status
```

应该显示：
```
Gateway: running
Feishu: OK
```

### 2.5.2 测试机器人

1. 在飞书搜索你的机器人名称
2. 发送消息：`你好`
3. 应该收到 AI 的回复

【图片 - 飞书聊天截图】

【信息框 - 绿色】
✅ 如果收到回复，说明部署成功！

---

## 2.6 部署后必做

### 2.6.1 创建纯净快照

【代码块 - bash】
```bash
ocs fresh
```

名称：`fresh_install`
类型：`纯净安装`

【信息框 - 蓝色】
📌 这是你的"救命稻草"，以后玩坏了可以恢复到这里

### 2.6.2 测试基本功能

【检查清单】
- [ ] 私聊机器人，能正常回复
- [ ] @机器人，能正常回复
- [ ] 让机器人执行简单任务（如"查看当前时间"）

---

## 2.7 常见问题

### Q: 部署卡在"安装 OpenClaw"

【折叠块：解决方案】
**可能原因：**
1. 网络问题
2. npm 权限问题

**解决：**
```bash
# 使用淘宝镜像
npm config set registry https://registry.npmmirror.com

# 或使用 npx
npx openclaw@latest onboard
```

### Q: 飞书收不到消息

【折叠块：排查步骤】
1. 检查应用是否已发布为「在线应用」
2. 检查事件订阅是否选择「长连接」
3. 检查权限是否全部开通
4. 检查 App ID / Secret 是否正确
5. 重启服务：`openclaw gateway restart`

### Q: Gateway 启动失败

【折叠块：排查步骤】
```bash
# 检查端口占用
lsof -i :18789

# 查看详细错误
openclaw gateway logs

# 手动启动看错误
openclaw gateway start
```

---

## 2.8 下一步

【按钮】
→ [第三章：备份与恢复](链接)

恭喜完成部署！现在学习如何保护你的劳动成果：
- 定期备份配置
- 导出到其他机器
- 恢复配置

---

*第二章完*

📊 **本章统计**
- 预计阅读时间：15分钟
- 预计操作时间：20分钟
- 难度：⭐⭐（中等）
