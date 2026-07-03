import re
from collections import Counter


STOP_WORDS = {
    "and",
    "for",
    "the",
    "with",
    "from",
    "this",
    "that",
    "are",
    "you",
    "your",
    "our",
    "can",
    "will",
    "into",
    "made",
    "product",
}


def extract_keywords(text, limit=20):
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9-]{2,}", text.lower())
    filtered = [word for word in words if word not in STOP_WORDS]
    return [word for word, _ in Counter(filtered).most_common(limit)]
