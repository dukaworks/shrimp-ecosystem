# 👨‍💻 开发者文档
# Developer Guide

> 欢迎加入虾族生态，一起打造更好的工具！

---

## 🎯 本文档目标

- 搭建开发环境
- 理解代码规范
- 掌握开发流程
- 发布你的工具

---

## 1. 开发环境搭建

### 1.1 基础要求

【信息框 - 蓝色】
📌 **系统要求**

- Python 3.7+
- Node.js 18+
- Git
- 代码编辑器（推荐 VSCode）
- 终端工具（iTerm2/Terminal/WSL）

### 1.2 克隆仓库

```bash
# 1. Fork 仓库（在 GitHub 上点击 Fork）

# 2. 克隆你的 Fork
git clone https://github.com/YOUR_USERNAME/openclaw-feishu-deployer.git
cd openclaw-feishu-deployer

# 3. 添加上游仓库
git remote add upstream https://github.com/dukaworks/openclaw-feishu-deployer.git
```

### 1.3 创建虚拟环境

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate     # Windows

# 安装开发依赖
pip install -e ".[dev]"

# 安装代码检查工具
pip install black flake8 pytest
```

### 1.4 验证环境

```bash
# 运行测试
pytest

# 检查代码格式
black --check .
flake8

# 运行工具
python -m openclaw_feishu_deployer --help
```

---

## 2. 项目结构

### 2.1 标准项目结构

```
openclaw-xxx-tool/              # 项目根目录
├── openclaw_xxx_tool/          # Python 包
│   ├── __init__.py             # 包初始化
│   ├── __main__.py             # 入口点
│   ├── cli.py                  # 命令行接口
│   └── core.py                 # 核心逻辑
├── tests/                      # 测试目录
│   ├── __init__.py
│   ├── test_cli.py
│   └── test_core.py
├── assets/                     # 资源文件
│   └── logo.svg
├── docs/                       # 文档
│   └── usage.md
├── .github/                    # GitHub 配置
│   └── workflows/
│       └── ci.yml              # CI/CD
├── .gitignore
├── LICENSE                     # MIT 许可证
├── README.md                   # 项目说明
├── setup.py                    # 包配置
├── requirements.txt            # 依赖
└── requirements-dev.txt        # 开发依赖
```

### 2.2 关键文件说明

【表格】
| 文件 | 用途 | 必须 |
|------|------|------|
| `setup.py` | 包配置、入口点 | ✅ |
| `__init__.py` | 版本号、导出 | ✅ |
| `__main__.py` | `python -m` 入口 | ✅ |
| `cli.py` | 命令行参数解析 | ✅ |
| `core.py` | 核心业务逻辑 | ✅ |
| `tests/` | 单元测试 | ✅ |
| `.github/workflows/ci.yml` | 自动化测试 | ✅ |

---

## 3. 开发新工具（六虾战队扩展）

### 3.1 工具命名规范

```python
# 命令缩写规则
deploy    -> ofd    (openclaw-feishu-deploy)
uninstall -> ocu    (openclaw-uninstall)
snapshot  -> ocs    (openclaw-snapshot)
health    -> och    (openclaw-health)
upgrade   -> ocg    (openclaw-upgrade)
config    -> occ    (openclaw-config)

# 格式: oc + 首字母
```

### 3.2 创建新工具脚手架

```bash
# 使用模板创建新工具
mkdir openclaw-health
cd openclaw-health

# 创建基础结构
mkdir -p openclaw_health tests assets .github/workflows
```

### 3.3 核心代码模板

【折叠块：cli.py 模板】
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🦞🏥 OpenClaw Health - 健康虾
诊断和监控 OpenClaw 运行状态
"""

import sys
import argparse
from .health_checker import HealthChecker

def main():
    parser = argparse.ArgumentParser(
        description='🦞🏥 OpenClaw 健康诊断工具',
        prog='och'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='子命令')
    
    # check 命令
    check_parser = subparsers.add_parser('check', help='全面健康检查')
    check_parser.add_argument('--verbose', '-v', action='store_true', help='详细输出')
    
    # doctor 命令
    doctor_parser = subparsers.add_parser('doctor', help='诊断问题')
    doctor_parser.add_argument('--fix', action='store_true', help='尝试自动修复')
    
    # status 命令
    status_parser = subparsers.add_parser('status', help='查看状态')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(0)
    
    checker = HealthChecker()
    
    if args.command == 'check':
        checker.full_check(verbose=args.verbose)
    elif args.command == 'doctor':
        checker.diagnose(auto_fix=args.fix)
    elif args.command == 'status':
        checker.show_status()

if __name__ == '__main__':
    main()
```

【折叠块：core.py 模板】
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
核心健康检查逻辑
"""

import os
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    END = '\033[0m'

class HealthChecker:
    """健康检查器"""
    
    def __init__(self):
        self.home = Path.home()
        self.openclaw_dir = self.home / '.openclaw'
        self.issues = []
        self.warnings = []
    
    def full_check(self, verbose=False):
        """全面检查"""
        print("🦞🏥 OpenClaw 健康检查\n")
        
        checks = [
            self._check_installation(),
            self._check_gateway_service(),
            self._check_config(),
            self._check_disk_space(),
            self._check_permissions(),
        ]
        
        passed = sum(checks)
        total = len(checks)
        
        print(f"\n{'='*50}")
        print(f"检查结果: {passed}/{total} 项通过")
        
        if self.issues:
            print(f"{Colors.RED}❌ 发现 {len(self.issues)} 个问题{Colors.END}")
            for issue in self.issues:
                print(f"  - {issue}")
        
        if self.warnings:
            print(f"{Colors.YELLOW}⚠️  {len(self.warnings)} 个警告{Colors.END}")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        if passed == total:
            print(f"{Colors.GREEN}✅ 一切正常！{Colors.END}")
        
        return len(self.issues) == 0
    
    def _check_installation(self) -> bool:
        """检查安装"""
        print("[1/5] 检查安装...", end=" ")
        
        if not self.openclaw_dir.exists():
            self.issues.append("OpenClaw 未安装")
            print(f"{Colors.RED}❌{Colors.END}")
            return False
        
        print(f"{Colors.GREEN}✅{Colors.END}")
        return True
    
    def _check_gateway_service(self) -> bool:
        """检查服务"""
        print("[2/5] 检查 Gateway 服务...", end=" ")
        
        try:
            result = subprocess.run(
                ['pgrep', '-f', 'openclaw'],
                capture_output=True
            )
            if result.returncode == 0:
                print(f"{Colors.GREEN}✅ 运行中{Colors.END}")
                return True
            else:
                self.warnings.append("Gateway 未运行")
                print(f"{Colors.YELLOW}⚠️  未运行{Colors.END}")
                return False
        except:
            self.issues.append("无法检查进程")
            print(f"{Colors.RED}❌{Colors.END}")
            return False
    
    def _check_config(self) -> bool:
        """检查配置"""
        print("[3/5] 检查配置...", end=" ")
        
        config_file = self.openclaw_dir / 'openclaw.json'
        if not config_file.exists():
            self.issues.append("配置文件不存在")
            print(f"{Colors.RED}❌{Colors.END}")
            return False
        
        # 检查 JSON 有效性
        try:
            import json
            with open(config_file) as f:
                json.load(f)
            print(f"{Colors.GREEN}✅{Colors.END}")
            return True
        except:
            self.issues.append("配置文件损坏")
            print(f"{Colors.RED}❌{Colors.END}")
            return False
    
    def _check_disk_space(self) -> bool:
        """检查磁盘空间"""
        print("[4/5] 检查磁盘空间...", end=" ")
        
        import shutil
        stat = shutil.disk_usage(self.home)
        free_gb = stat.free / (1024**3)
        
        if free_gb < 1:
            self.warnings.append(f"磁盘空间不足: {free_gb:.1f}GB")
            print(f"{Colors.YELLOW}⚠️  {free_gb:.1f}GB{Colors.END}")
            return False
        
        print(f"{Colors.GREEN}✅ {free_gb:.1f}GB{Colors.END}")
        return True
    
    def _check_permissions(self) -> bool:
        """检查权限"""
        print("[5/5] 检查权限...", end=" ")
        
        if os.access(self.openclaw_dir, os.W_OK):
            print(f"{Colors.GREEN}✅{Colors.END}")
            return True
        else:
            self.issues.append("无写入权限")
            print(f"{Colors.RED}❌{Colors.END}")
            return False
    
    def diagnose(self, auto_fix=False):
        """诊断问题"""
        print("🔍 诊断模式\n")
        
        self.full_check()
        
        if auto_fix and self.issues:
            print("\n🛠️  尝试自动修复...")
            # 实现自动修复逻辑
            pass
    
    def show_status(self):
        """显示状态"""
        print("📊 OpenClaw 状态\n")
        # 实现状态显示
```

### 3.4 setup.py 模板

```python
#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="openclaw-health",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="🦞🏥 OpenClaw 健康诊断工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/openclaw-health",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "openclaw-health=openclaw_health.cli:main",
            "och=openclaw_health.cli:main",
        ],
    },
)
```

---

## 4. 代码规范

### 4.1 Python 代码风格

```python
# ✅ 正确的示例
from typing import Optional, List, Dict

def check_service(
    service_name: str,
    timeout: int = 30,
    verbose: bool = False
) -> Dict[str, bool]:
    """
    检查服务状态
    
    Args:
        service_name: 服务名称
        timeout: 超时时间（秒）
        verbose: 是否显示详细信息
        
    Returns:
        包含检查结果的字典
    """
    result = {"running": False, "healthy": False}
    
    # 检查逻辑
    if verbose:
        print(f"检查 {service_name}...")
    
    return result

# ❌ 错误的示例
def check(s, t=30, v=False):
    # 缺少类型注解
    # 缺少文档字符串
    # 变量名不清晰
    r = {"r": False}
    return r
```

### 4.2 提交信息规范

```bash
# 格式: emoji type: 描述

git commit -m "🦞 feat: 添加健康检查功能"
git commit -m "🐛 fix: 修复进程检测bug"
git commit -m "📚 docs: 更新使用说明"
git commit -m "💅 style: 代码格式化"
git commit -m "♻️ refactor: 重构检查逻辑"
git commit -m "🧪 test: 添加单元测试"
git commit -m "🔧 chore: 更新依赖版本"
```

【表格】
| Emoji | Type | 用途 |
|-------|------|------|
| 🦞 | feat | 新功能 |
| 🐛 | fix | Bug 修复 |
| 📚 | docs | 文档 |
| 💅 | style | 格式调整 |
| ♻️ | refactor | 重构 |
| 🧪 | test | 测试 |
| 🔧 | chore | 构建/工具 |

### 4.3 文档字符串规范

```python
def example_function(param1: str, param2: int) -> bool:
    """
    简短描述（一行）
    
    详细描述（多行），说明函数做什么、
    如何使用、注意事项等。
    
    Args:
        param1: 第一个参数说明
        param2: 第二个参数说明
        
    Returns:
        返回值说明
        
    Raises:
        ValueError: 什么时候抛出这个错误
        
    Example:
        >>> example_function("test", 42)
        True
    """
    pass
```

---

## 5. 测试规范

### 5.1 测试文件结构

```python
# tests/test_health_checker.py
import pytest
from openclaw_health.health_checker import HealthChecker

class TestHealthChecker:
    """HealthChecker 测试类"""
    
    def setup_method(self):
        """每个测试前执行"""
        self.checker = HealthChecker()
    
    def test_check_installation_success(self):
        """测试安装检查 - 成功情况"""
        # Mock 测试
        result = self.checker._check_installation()
        assert isinstance(result, bool)
    
    def test_check_config_valid(self, tmp_path):
        """测试配置检查 - 有效配置"""
        # 创建临时配置文件
        config_file = tmp_path / "openclaw.json"
        config_file.write_text('{"version": "1.0"}')
        
        self.checker.openclaw_dir = tmp_path
        result = self.checker._check_config()
        assert result is True
    
    def test_check_config_invalid(self, tmp_path):
        """测试配置检查 - 无效配置"""
        config_file = tmp_path / "openclaw.json"
        config_file.write_text('invalid json')
        
        self.checker.openclaw_dir = tmp_path
        result = self.checker._check_config()
        assert result is False
```

### 5.2 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_health_checker.py

# 运行并显示覆盖率
pytest --cov=openclaw_health --cov-report=html

# 调试模式
pytest -v --pdb
```

---

## 6. 发布流程

### 6.1 版本号规范

使用语义化版本（Semantic Versioning）：

```
主版本号.次版本号.修订号
1.0.0

- 主版本号：重大更新，不兼容旧版
- 次版本号：新功能，兼容旧版
- 修订号：Bug 修复
```

### 6.2 发布步骤

```bash
# 1. 更新版本号
# 编辑 __init__.py 和 setup.py

# 2. 更新 CHANGELOG.md
# 记录本次更新内容

# 3. 提交代码
git add .
git commit -m "🚀 release: v1.1.0"
git push

# 4. 创建标签
git tag v1.1.0
git push origin v1.1.0

# 5. 构建包
python setup.py sdist bdist_wheel

# 6. 上传到 PyPI
pip install twine
twine upload dist/*

# 7. 在 GitHub 创建 Release
# 填写发布说明
```

### 6.3 CI/CD 配置

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        pip install build twine
    
    - name: Build and publish
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: |
        python -m build
        twine upload dist/*
```

---

## 7. 调试技巧

### 7.1 本地调试

```bash
# 安装本地开发版本
pip install -e .

# 修改代码后立即生效（无需重新安装）

# 使用 ipdb 调试
pip install ipdb

# 在代码中插入
import ipdb; ipdb.set_trace()
```

### 7.2 日志调试

```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# 使用
logger.debug("调试信息")
logger.info("普通信息")
logger.warning("警告")
logger.error("错误")
```

---

## 8. 贡献检查清单

提交 PR 前检查：

【检查清单】
- [ ] 代码通过 `black` 格式化
- [ ] 代码通过 `flake8` 检查
- [ ] 所有测试通过 `pytest`
- [ ] 添加了新功能的测试
- [ ] 更新了文档（README、CHANGELOG）
- [ ] 提交了信息符合规范
- [ ] 代码有适当的注释和文档字符串
- [ ] 没有提交敏感信息（密码、token）

---

## 9. 常见问题

### Q: 如何测试与 OpenClaw 的交互？

使用 Mock：

```python
from unittest.mock import Mock, patch

@patch('subprocess.run')
def test_gateway_start(mock_run):
    mock_run.return_value = Mock(returncode=0)
    result = start_gateway()
    assert result is True
```

### Q: 如何处理跨平台差异？

```python
import platform
import os

if platform.system() == 'Windows':
    config_dir = os.path.expandvars(r'%USERPROFILE%\.openclaw')
elif platform.system() == 'Darwin':  # macOS
    config_dir = os.path.expanduser('~/.openclaw')
else:  # Linux
    config_dir = os.path.expanduser('~/.openclaw')
```

### Q: 如何添加新的 CLI 命令？

在 `cli.py` 中添加 subparser：

```python
new_cmd = subparsers.add_parser('newcmd', help='新命令说明')
new_cmd.add_argument('--option', help='选项说明')
```

---

## 10. 资源推荐

### 学习资源

- **Python 官方文档**: https://docs.python.org/3/
- **Click 文档** (CLI 框架): https://click.palletsprojects.com/
- **Pytest 文档**: https://docs.pytest.org/
- **Black 代码格式化**: https://black.readthedocs.io/

### 工具推荐

- **VSCode**: 代码编辑器 + Python 插件
- **PyCharm**: Python IDE
- **Postman**: API 测试
- **Docker**: 环境隔离

---

## 11. 联系开发者

有问题？

- **GitHub Issues**: 提交问题
- **飞书群**: 实时讨论
- **邮件**: chenzhy.bj@gmail.com

---

🦞 **欢迎加入虾族生态开发者大家庭！**