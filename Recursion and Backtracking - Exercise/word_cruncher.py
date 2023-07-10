def find_combinations(idx, target, words_count, words_by_idx, used_words):
    if idx >= len(target):
        print(" ".join(used_words))
        return

    if idx not in words_by_idx:
        return

    for word in words_by_idx[idx]:
        if words_count[word] == 0:
            continue

        used_words.append(word)
        words_count[word] -= 1

        find_combinations(idx + len(word), target, words_count, words_by_idx, used_words)

        used_words.pop()
        words_count[word] += 1

words = input().split(", ")
target = input()

words_count = {}  # "word": count
words_by_idx = {}  # "idx": [words]

for word in words:
    if word in words_count:
        words_count[word] += 1
        continue

    words_count[word] = 1

    try:
        idx = 0
        while True:
            idx = target.index(word, idx)

            if idx not in words_by_idx:
                words_by_idx[idx] = []

            words_by_idx[idx].append(word)
            idx += len(word)

    except ValueError:
        pass

find_combinations(0, target, words_count, words_by_idx, [])
