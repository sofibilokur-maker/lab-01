import os
import time
import tracemalloc
import json
from collections import Counter
from findex.docum_read import iter_documents
from findex.tokens import tokenize


def collect_stats_streaming(corpus_dir: str = "data"):
    tracemalloc.start()
    start_time = time.perf_counter()

    doc_count = 0
    token_count = 0
    vocab = Counter()

    for doc in iter_documents(corpus_dir):
        doc_count += 1
        for token in tokenize(doc):
            token_count += 1
            vocab[token] += 1

    elapsed = time.perf_counter() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "doc_count": doc_count,
        "token_count": token_count,
        "vocab_size": len(vocab),
        "top_50": vocab.most_common(50),
        "elapsed_sec": elapsed,
        "peak_memory_mb": peak / 1024 / 1024,
    }


if __name__ == "__main__":
    import json
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    DATA_DIR = os.path.join(PROJECT_ROOT, "data")

    result = collect_stats_streaming(DATA_DIR)
    print(f"Документів: {result['doc_count']}")
    print(f"Токенів: {result['token_count']}")
    print(f"Розмір словника: {result['vocab_size']}")
    print(f"Час: {result['elapsed_sec']:.2f} сек")
    print(f"Пікова пам'ять: {result['peak_memory_mb']:.2f} МБ")
    print("\nТоп-50 термів:")
    for word, freq in result["top_50"]:
        print(f"  {word}: {freq}")

    result_path = os.path.join(PROJECT_ROOT, "results_sts.json")
    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\nРезультат збережено: {result_path}")