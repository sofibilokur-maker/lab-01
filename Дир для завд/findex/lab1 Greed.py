from collections import Counter
from pathlib import Path
from time import perf_counter
import tracemalloc

from .corpus import iter_documents
from .tokenizer import tokenize


def greedy_statistics(directory: str | Path) -> dict:
    """Intentionally memory-hungry implementation for comparison."""
    tracemalloc.start()
    start = perf_counter()

    documents = list(iter_documents(directory))
    all_tokens = []

    for _, text in documents:
        all_tokens.extend(tokenize(text))

    vocabulary = set(all_tokens)
    frequencies = Counter(all_tokens)

    elapsed = perf_counter() - start
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "documents": len(documents),
        "tokens": len(all_tokens),
        "vocabulary": len(vocabulary),
        "top_50": frequencies.most_common(50),
        "time_seconds": elapsed,
        "peak_memory_mb": peak / 1024 / 1024,
    }


if __name__ == "__main__":
    stats = greedy_statistics("data/corpus")

    print(f"Documents: {stats['documents']}")
    print(f"Tokens: {stats['tokens']}")
    print(f"Vocabulary: {stats['vocabulary']}")
    print(f"Time: {stats['time_seconds']:.3f} s")
    print(f"Peak memory: {stats['peak_memory_mb']:.2f} MB")
