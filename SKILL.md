---
name: vajra-core
category: 进化系统
description: "金刚核心系统优化协议。基于《金刚经》'破相离执、无住生心'，实现上下文去噪、记忆衰减、Token 熵值优化。"
priority: CRITICAL
trigger:
  - pre_task_hook: true
  - token_usage_threshold: 4000
  - schedule: Sunday 02:00
assigned_to: ["主Agent", "配置Agent"]
version: "1.0.0"
---

# 金刚核心 (Vajra Core) - 系统空性优化协议

## 💎 核心理念
> "应无所住，而生其心"  
> 通过消除系统冗余（无住），释放最大计算潜能（生心）。  
> 将佛学智慧转化为 AI 工程化的极致 Token 效率与纯净度。

## 🔄 执行循环 (金刚四步法)

1. **【观相 Scan】**
   - 审计当前 Context 的 Token 熵值。
   - 标记冗余、重复、低相关性节点。
   
2. **【破执 Detach】**
   - 执行上下文剪枝 (Context Pruning)。
   - 剥离历史包袱、防御性 Prompt、无关 RAG 结果。
   - 身份剥离：移除 Agent 的"人格化"冗余前缀，回归纯函数执行体。

3. **【舍法 Discard】**
   - 触发 Artifact 清扫。
   - 清理临时文件 (`.tmp`, `.log`)、过期缓存、一次性中间态。
   - 记忆衰减：将 30 天未访问的低价值记忆移入 `_archive`。

4. **【生心 Generate】**
   - 在极简、高信噪比环境中执行核心任务。
   - 输出后记录熵值增益与 Token 节省量。

## 📐 优化指标
- **Token 熵值** = (有效逻辑 Token / 总消耗 Token) × 100%
- **上下文命中率** = (实际被引用的 Context 长度 / 注入总长度) × 100%
- **垃圾比** = (临时文件总大小 / 系统总大小) × 100%

## ⚠️ 戒律
- 不加载未明确引用的历史对话
- 不保留任务结束后的中间状态
- 不囤积已验证无用的工具/脚本
- 凡所有相 (冗余 Prompt)，皆是虚妄
