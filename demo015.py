import re
from typing import List


def smart_split(text: str, max_len: int = 8000) -> List[str]:
    """
    智能分片函数（保持段落语义完整）
    策略：优先按段落分割，其次按句子分割
    """
    chunks = []

    # 第一级分割：按双换行符分割段落
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]

    current_chunk = ""
    for p in paragraphs:
        # 段落自身超过限制
        if len(p) > max_len:
            # 第二级分割：按句子分割
            sentences = re.split(r'(?<=[.!?。！？])\s+', p)
            for s in sentences:
                if len(current_chunk) + len(s) > max_len and current_chunk:
                    chunks.append(current_chunk)
                    current_chunk = s
                else:
                    current_chunk += s + " "
        # 段落可加入当前分片
        elif len(current_chunk) + len(p) > max_len and current_chunk:
            chunks.append(current_chunk)
            current_chunk = p
        else:
            current_chunk += p + "\n\n"

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def process_text_for_dify(text: str, max_len: int = 8000):
    """
    处理文本以适配Dify工作流的分片逻辑
    """
    # --- 核心分片逻辑（适配Dify工作流）---
    if len(text) > max_len:
        # 生成分片（仅分割不处理）
        chunks = smart_split(text, max_len=max_len)

        # 添加分片元信息（为后续迭代做准备）
        chunks = [{"text": chunk, "chunk_id": f"chunk_{i + 1}/{len(chunks)}"}
                  for i, chunk in enumerate(chunks)]
    else:
        # 短文本直接包装为分片格式
        chunks = [{"text": text, "chunk_id": "single_chunk"}]

    return chunks
