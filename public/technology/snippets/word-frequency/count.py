import sys
from collections import Counter
import re


def count_words(text: str) -> Counter:
    words = re.findall(r"\b[a-z']+\b", text.lower())
    return Counter(words)


def top_n(counter: Counter, n: int = 10) -> list[tuple[str, int]]:
    return counter.most_common(n)


if __name__ == "__main__":
    text = sys.stdin.read()
    counts = count_words(text)

    print(f"{'Word':<20} {'Count':>6}")
    print("-" * 28)
    for word, count in top_n(counts):
        print(f"{word:<20} {count:>6}")
