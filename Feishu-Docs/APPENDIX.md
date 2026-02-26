# 📎 附录

> 快速参考手册

---

## A. 命令速查表

### 一键安装所有工具

```bash
pip install openclaw-feishu-deployer openclaw-uninstaller openclaw-snapshot
```

### 核心命令速查

| 场景 | 命令 |
|------|------|
| **部署** | `ofd deploy` |
| **创建快照** | `ocs create` 或 `ocs fresh` |
| **列出快照** | `ocs list` |
| **恢复快照** | `ocs restore <ID>` |
| **导出快照** | `ocs export <ID>` |
| **导入快照** | `ocs import <file>` |
| **卸载** | `ocu` |
| **查看状态** | `openclaw status` |
| **重启服务** | `openclaw gateway restart` |
| **查看日志** | `openclaw gateway logs` |

---

## B. 配置文件参考

### OpenClaw 主配置路径

```
~/.openclaw/openclaw.json
```

### 关键配置项

```json
{
  "gateway": {
    "bind": "127.0.0.1:18789",
    "auth": {
      "token": "your-secret-token"
    }
  },
  "channels": {
    "feishu": {
      "enabled": true,
      "appId": "cli_xxxxx",
      "appSecret": "xxxxx",
      "domain": "larkoffice.com"
    }
  },
  "models": {
    "providers": {
      "kimi": {
        "enabled": true,
        "apiKey": "sk-xxxxx"
      }
    }
  }
}
```

---

## C. 故障码对照

| 错误信息 | 可能原因 | 解决方案 |
|----------|----------|----------|
| `Gateway not running` | 服务未启动 | `openclaw gateway start` |
| `Port 18789 in use` | 端口被占用 | 查找并停止占用进程 |
| `Feishu auth failed` | 飞书凭证错误 | 检查 App ID / Secret |
| `API key invalid` | AI 模型密钥错误 | 更新 API Key |
| `Permission denied` | 权限不足 | 检查文件权限或加 sudo |
| `No space left` | 磁盘已满 | 清理磁盘空间 |

---

## D. 相关资源链接

### 官方资源

- **OpenClaw 官网**: https://openclaw.ai
- **OpenClaw 文档**: https://docs.openclaw.ai
- **飞书开放平台**: https://open.feishu.cn

### 虾族生态

- **生态文档**: https://github.com/dukaworks/shrimp-ecosystem
- **部署工具**: https://github.com/dukaworks/openclaw-feishu-deployer
- **卸载工具**: https://github.com/dukaworks/openclaw-uninstaller
- **备份工具**: https://github.com/dukaworks/openclaw-snapshot

### 社区

- **GitHub Discussions**: （待添加）
- **飞书社区**: （待添加）

---

*附录完*
