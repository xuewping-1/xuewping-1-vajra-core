import logging
from pathlib import Path
from datetime import datetime, timedelta
import shutil
import os

# 配置日志
logger = logging.getLogger("vajra_core")
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


class VajraOptimizer:
    """
    金刚核心优化器 (Vajra Optimizer)
    核心理念：应无所住，而生其心
    功能：上下文剪枝、记忆衰减、临时文件清扫、Token 熵值计算
    """
    
    def __init__(self, project_root: Path = None):
        # 如果未指定根目录，默认使用当前工作目录
        self.root = project_root or Path.cwd()
        
        # 定义默认目录结构（可配置）
        self.memory_dir = self.root / "memory"
        self.archive_dir = self.root / "archive"
        self.tmp_dir = self.root / "tmp"
        self.logs_dir = self.root / "logs"
        
        # 自动创建必要目录
        self.archive_dir.mkdir(parents=True, exist_ok=True)
        self.tmp_dir.mkdir(parents=True, exist_ok=True)

    def scan_entropy(self, context_tokens: list) -> float:
        """
        【观相】计算当前上下文的 Token 熵值
        启发式算法：系统指令/历史重复/低信息密度标记为低熵
        """
        if not context_tokens: 
            return 0.0
        
        # 简单的熵值计算模型：
        # 1. 用户指令 (User Role) 通常包含高熵信息
        # 2. 系统提示 (System Role) 熵值中等
        # 3. 重复内容或极短回复熵值极低
        
        total_tokens = len(context_tokens)
        high_info_count = 0
        
        for t in context_tokens:
            content = t.get('content', '')
            role = t.get('role', '')
            
            # 长度过滤
            if len(content.strip()) < 10:
                continue
                
            # 角色加权
            if role == 'user':
                high_info_count += 1.0
            elif role == 'system':
                high_info_count += 0.6
            elif role == 'assistant':
                # 助手回复如果包含大量代码或长文本，也算有效
                if len(content) > 100:
                    high_info_count += 0.8
                else:
                    high_info_count += 0.2
                    
        entropy = (high_info_count / total_tokens) * 100 if total_tokens > 0 else 0
        logger.info(f"[Vajra Scan] Context Entropy: {entropy:.1f}%")
        return entropy

    def prune_context(self, context: list, max_rounds: int = 5) -> list:
        """
        【破执】滑动窗口剪枝
        仅保留最近 N 轮对话，剥离过远的历史包袱
        """
        if not context: return []
        
        # 简单策略：保留最新的 N 条消息
        # 实际应用中可接入 tiktoken 进行 Token 精确截断
        pruned = context[-max_rounds:]
        
        logger.info(f"[Vajra Prune] Context reduced: {len(context)} -> {len(pruned)} items")
        return pruned

    def memory_decay(self, days_inactive: int = 30) -> int:
        """
        【舍法】过去心不可得：归档低活跃度记忆
        """
        cutoff = datetime.now() - timedelta(days=days_inactive)
        archived_count = 0
        
        if not self.memory_dir.exists():
            return 0
            
        for mem_file in self.memory_dir.rglob("*.json"):
            try:
                mtime = datetime.fromtimestamp(mem_file.stat().st_mtime)
                if mtime < cutoff:
                    archive_path = self.archive_dir / mem_file.name
                    # 避免重名覆盖
                    if archive_path.exists():
                        archive_path = archive_path.with_stem(f"{mem_file.stem}_{mtime.strftime('%Y%m%d')}")
                    
                    shutil.move(str(mem_file), str(archive_path))
                    archived_count += 1
                    logger.info(f"[Vajra Archive] {mem_file.name} -> _archive/")
            except Exception as e:
                logger.error(f"[Vajra Error] Failed to archive {mem_file.name}: {e}")
                
        logger.info(f"[Vajra Decay] Archived {archived_count} sleeping memories")
        return archived_count

    def sweep_artifacts(self) -> int:
        """
        【舍法】法如筏喻：清理临时文件与中间态
        """
        swept_count = 0
        
        # 1. 清理 logs/agents 目录中超过 7 天的日志
        if self.logs_dir.exists():
            log_cutoff = datetime.now() - timedelta(days=7)
            for log_file in self.logs_dir.iterdir():
                try:
                    mtime = datetime.fromtimestamp(log_file.stat().st_mtime)
                    if mtime < log_cutoff and log_file.suffix == '.json':
                        log_file.unlink()
                        swept_count += 1
                except Exception:
                    pass
                    
        # 2. 清理 tmp 目录
        if self.tmp_dir.exists():
            for f in self.tmp_dir.iterdir():
                try:
                    if f.is_file():
                        f.unlink()
                        swept_count += 1
                    elif f.is_dir():
                        shutil.rmtree(f)
                        swept_count += 1
                except Exception:
                    pass
                    
        logger.info(f"[Vajra Sweep] Cleaned {swept_count} artifacts")
        return swept_count

    def execute_cycle(self, context: list = None) -> dict:
        """
        【生心】完整金刚循环
        """
        logger.info("=" * 60)
        logger.info("[VAJRA] 启动金刚核心优化循环")
        logger.info("=" * 60)
        
        result = {
            "status": "optimized",
            "actions_taken": [],
            "entropy_gain": "N/A",
            "context_reduction": "N/A",
        }
        
        # 1. 扫描
        if context:
            entropy_before = self.scan_entropy(context)
            pruned = self.prune_context(context)
            entropy_after = self.scan_entropy(pruned)
            result["entropy_gain"] = f"{entropy_before:.1f}% -> {entropy_after:.1f}%"
            result["context_reduction"] = f"{len(context)} -> {len(pruned)} items"
            result["actions_taken"].append("context_pruned")
        
        # 2. 归档记忆 (过去心不可得)
        archived = self.memory_decay()
        if archived > 0:
            result["actions_taken"].append(f"archived_{archived}_memories")
            
        # 3. 清扫垃圾 (法如筏喻)
        swept = self.sweep_artifacts()
        if swept > 0:
            result["actions_taken"].append(f"swept_{swept}_artifacts")
            
        logger.info(f"[VAJRA] 优化完成: {result}")
        return result


if __name__ == "__main__":
    # 通用运行模式：基于当前工作目录
    optimizer = VajraOptimizer()
    
    # 模拟测试上下文
    mock_context = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Analyze the following data..."},
        {"role": "assistant", "content": "Sure, here is the analysis."},
    ]
    
    optimizer.execute_cycle(mock_context)
