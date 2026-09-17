import argparse
from collections import Counter

def count_words(text, ignore_case=False):
    if ignore_case:
        text = text.lower()
    words = text.split()
    return Counter(words)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="统计文本中出现次数最多的词")
    parser.add_argument("input_file", help="要统计的 UTF-8 文本文件")
    parser.add_argument(
        "-c",
        "--ignore-case",
        action="store_true",
        help="统计时忽略大小写",
    )
    args = parser.parse_args()

    with open(args.input_file, encoding="utf-8") as file:
        text = file.read()
    stats = count_words(text, ignore_case=args.ignore_case)
    for word, count in stats.most_common(10):
        print(f"{word}: {count}")
