from datasets import load_dataset
import os

CORPUS_DIR = "data"
MAX_FILES = 1000
MAX_SIZE_BYTES = 50 * 1024 * 1024  # 50 МБ

os.makedirs(CORPUS_DIR, exist_ok=True)

ds = load_dataset("common-pile/project_gutenberg", split="train", streaming=True)

total_size = 0
count = 0

for item in ds:
    text = item.get("text")
    if not text:
        continue

    path = os.path.join(CORPUS_DIR, f"book_{count:04d}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    total_size += len(text.encode("utf-8"))
    count += 1

    if count % 50 == 0:
        print(f"...{count} файлів, {total_size / 1024 / 1024:.1f} МБ")

    if count >= MAX_FILES or total_size >= MAX_SIZE_BYTES:
        break

print(f"\nГотово: {count} файлів, {total_size / 1024 / 1024:.1f} МБ у папці {CORPUS_DIR}/")