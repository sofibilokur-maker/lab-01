"""documents.py — потоковий читач корпусу документів."""

import os
from typing import Iterator

def iter_documents(corpus_dir: str = "data") -> Iterator[str]:
    """
    Генератор, що читає документи по одному з папки corpus_dir.
    Не завантажує весь корпус у пам'ять — кожен файл читається,
    віддається через yield, і звільняється перед наступним.
    """
    filenames = sorted(os.listdir(corpus_dir))
    for filename in filenames:
        if not filename.endswith(".txt"):
            continue
        path = os.path.join(corpus_dir, filename)
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            yield f.read()


            