import os
import json


def load_results(path):
    if not os.path.exists(path):
        raise FileNotFoundError(
            "Файл не знайдено: " + path
        )

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():

    project_root = os.path.dirname(
        os.path.abspath(__file__)
    )

    streaming_file = os.path.join(
        project_root,
        "results_sts.json"
    )

    greedy_file = os.path.join(
        project_root,
        "results_greedy.json"
    )

    streaming = load_results(streaming_file)
    greedy = load_results(greedy_file)

    streaming_time = streaming.get(
        "elapsed_sec", 0
    )

    streaming_memory = streaming.get(
        "peak_memory_mb", 0
    )

    streaming_documents = streaming.get(
        "doc_count", 0
    )

    streaming_terms = streaming.get(
        "vocab_size", 0
    )

    greedy_time = greedy.get(
        "elapsed_sec", 0
    )

    greedy_memory = greedy.get(
        "peak_memory_mb", 0
    )

    greedy_documents = greedy.get(
        "doc_count", 0
    )

    greedy_terms = greedy.get(
        "vocab_size", 0
    )

    lines = []

    lines.append("# findex")
    lines.append("")

    lines.append(
        "Проєкт для побудови текстового індексу корпусу книг."
    )

    lines.append("")

    lines.append(
        "Порівнюються два підходи до обробки тексту:"
    )

    lines.append("")

    lines.append(
        "- Streaming — потокова обробка за допомогою генераторів."
    )

    lines.append(
        "- Greedy — обробка даних із використанням списків."
    )

    lines.append("")

    lines.append("## Таблиця вимірювань")
    lines.append("")

    lines.append(
        "| Показник | Streaming | Greedy |"
    )

    lines.append(
        "|---|---:|---:|"
    )

    lines.append(
        "| Кількість документів | "
        + str(streaming_documents)
        + " | "
        + str(greedy_documents)
        + " |"
    )

    lines.append(
        "| Кількість унікальних термінів | "
        + str(streaming_terms)
        + " | "
        + str(greedy_terms)
        + " |"
    )

    lines.append(
        "| Час виконання, сек | "
        + f"{streaming_time:.4f}"
        + " | "
        + f"{greedy_time:.4f}"
        + " |"
    )

    lines.append(
        "| Пікове використання пам'яті, MB | "
        + f"{streaming_memory:.2f}"
        + " | "
        + f"{greedy_memory:.2f}"
        + " |"
    )

    lines.append("")

    lines.append("## Висновок")
    lines.append("")

    lines.append(
        "Streaming використовує генератори для потокової "
        "обробки документів."
    )

    lines.append("")

    lines.append(
        "Greedy використовує списки для зберігання даних "
        "під час обробки."
    )

    lines.append("")

    lines.append(
        "За результатами вимірювань можна порівняти "
        "час виконання та використання оперативної пам'яті "
        "двох підходів."
    )

    readme_content = "\n".join(lines)

    readme_file = os.path.join(
        project_root,
        "README.md"
    )

    with open(
        readme_file,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(readme_content)

    print("README.md успішно створено!")
    print(readme_file)


if __name__ == "__main__":
    main()