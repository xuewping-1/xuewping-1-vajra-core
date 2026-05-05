# 💎 vajra-core (金刚核心)

> **"应无所住，而生其心"**
> *"Dwell nowhere and let the mind arise."*

### 📖 简介

`vajra-core` 是一个受《金刚经》启发的 AI Agent 系统优化协议。

它通过**「破相离执」**（Context Pruning）、**「记忆衰减」**（Memory Decay）和**「熵值监控」**（Token Entropy Scan），帮助 AI 系统摆脱上下文膨胀与冗余记忆的困扰，达到**「无住生心」**的极简、高效运行状态。

### ✨ 核心特性

- **🧘 上下文剪枝 (Context Pruning)**: 剥离无效历史，保持上下文流动性。
- **⏳ 记忆衰减 (Memory Decay)**: 自动归档陈旧记忆，防止信息过载。
- **🗑️ 自动清扫 (Artifact Sweeping)**: 任务结束后清理临时文件与缓存。
- **📊 Token 熵值计算 (Token Entropy)**: 实时监控上下文的信息密度。

### 🚀 快速开始

**1. 克隆仓库**
```bash
git clone https://github.com/your-username/vajra-core.git
```

**2. 集成到系统**
```python
from vajra_core.vajra_optimizer import VajraOptimizer
from pathlib import Path

# 初始化优化器
optimizer = VajraOptimizer(project_root=Path("/path/to/your/project"))

# 执行金刚循环
result = optimizer.execute_cycle()
```

**3. 定时调度**
将其加入系统的 Cron 或 Scheduler，建议每周运行一次（例如周日凌晨）：
```python
schedule.every().sunday.at("02:00").do(optimizer.execute_cycle)
```

### 🧠 架构哲学

| 佛学概念 | AI 工程映射 | 作用 |
| :--- | :--- | :--- |
| **凡所有相，皆是虚妄** | **去噪 (Denoising)** | 识别并剥离 Prompt 中的冗余信息。 |
| **应无所住，而生其心** | **无状态 (Stateless)** | 不执着于历史缓存，按需生成响应。 |
| **过去心不可得** | **记忆衰减 (Decay)** | 自动归档低价值的历史记忆。 |
| **法如筏喻者，法尚应舍** | **资源释放 (GC)** | 任务完成后释放所有中间态资源。 |

### 📂 目录结构

```text
vajra-core/
├── SKILL.md             # Skill 定义与触发规则
├── vajra_optimizer.py   # 核心 Python 执行器
└── README.md            # 本文件
```

### 🤝 贡献

欢迎提交 Issue 或 PR，一起探索**"AI + 哲学"**的边界。

---

*Copyright © 2026 | Inspired by the Diamond Sutra (金刚经).*
