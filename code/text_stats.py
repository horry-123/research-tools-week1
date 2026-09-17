"""统计 UTF-8 文本文件中的英文单词频率。"""

import argparse
import re
from collections import Counter
from pathlib import Path


def count_words(text: str, ignore_case: bool = False) -> Counter[str]:
    """返回文本中单词及其出现次数。"""
    if ignore_case:
        text = text.lower()
    words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text)
    return Counter(words)


def main() -> None:
    parser = argparse.ArgumentParser(description="统计文本文件中的单词频率")
    parser.add_argument("input_file", type=Path, help="要统计的 UTF-8 文本文件")
    parser.add_argument(
        "-c",
        "--ignore-case",
        action="store_true",
        help="统计时忽略大小写",
    )
    args = parser.parse_args()

    try:
        text = args.input_file.read_text(encoding="utf-8")
    except OSError as error:
        parser.error(f"无法读取文件 {args.input_file}: {error}")

    frequencies = count_words(text, ignore_case=args.ignore_case)
    for word, count in sorted(frequencies.items(), key=lambda item: (-item[1], item[0])):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
