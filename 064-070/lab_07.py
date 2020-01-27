from collections import Counter


INPUT_FILE = "moby_01_clean.txt"

if __name__ == '__main__':
    with open(INPUT_FILE) as fin:
        words = fin.read().splitlines(keepends=False)
    counter_words = Counter(words)

    print("collections.Counter implementation:")
    print(f"5 most common words: {counter_words.most_common(5)}\n"
          f"5 rarest words: {counter_words.most_common()[-5:]}")

    counter_words = {}
    for w in words:
        counter_words[w] = counter_words.get(w, 0) + 1
    sorted_words = sorted(counter_words.items(),
                          key=lambda x: x[1],
                          reverse=True)
    print("dict implementation:")
    print(f"5 most common words: {sorted_words[:5]}\n"
          f"5 rarest words: {sorted_words[-5:]}")
