import sys
from collections import Counter

def count_words(text):
    words = text.split()
    return Counter(words)

if __name__ == "__main__":
    text = open(sys.argv[1], encoding="utf-8").read()
    stats = count_words(text)
    for word, count in stats.most_common(10):
        print(f"{word}: {count}")