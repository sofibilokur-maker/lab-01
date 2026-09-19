import os
import time
import tracemalloc
import unicodedata
import re
from collections import Counter

_TOKEN_PATTERN = re.compile(r"\d+[.,]\d+|\d+|[^\W\d_]+(?:['\-][^\W\d_]+)*", re.UNICODE)


def collect_stats_greedy(corpus_dir: str = "data"):
    tracemalloc.start()
    start_time = time.perf_counter()

    filenames = sorted(f for f in os.listdir(corpus_dir) if f.endswith(".txt"))
    all_docs = []
    for filename in filenames:
        with open(os.path.join(corpus_dir, filename), "r", encoding="utf-8", errors="ignore") as f:
            all_docs.append(f.read())

    all_tokens = []
    for doc in all_docs:
        normalized = unicodedata.normalize("NFKC", doc).lower()
        all_tokens.extend(_TOKEN_PATTERN.findall(normalized))  # ще один повний список у пам'яті

    # 3. Рахуємо словник
    vocab = Counter(all_tokens)

    elapsed = time.perf_counter() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "doc_count": len(all_docs),
        "token_count": len(all_tokens),
        "vocab_size": len(vocab),
        "top_50": vocab.most_common(50),
        "elapsed_sec": elapsed,
        "peak_memory_mb": peak / 1024 / 1024,
    }


if __name__ == "__main__":
    import json

    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    DATA_DIR = os.path.join(PROJECT_ROOT, "data")

    result = collect_stats_greedy(DATA_DIR)
    print(f"Документів: {result['doc_count']}")
    print(f"Токенів: {result['token_count']}")
    print(f"Розмір словника: {result['vocab_size']}")
    print(f"Пікова пам'ять: {result['peak_memory_mb']:.2f} МБ")
    print(f"Час: {result['elapsed_sec']:.2f} сек")
    print("\nТоп-50 термів:")
    for word, freq in result["top_50"]:
        print(f"  {word}: {freq}")

    result_path = os.path.join(PROJECT_ROOT, "results_greedy.json")
    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\nРезультат збережено: {result_path}")