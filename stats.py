def get_num_words(s):
    return len(s.split())

def count_characters(s):
    counts = {}
    for c in s:
        if not c.isalpha(): continue
        counts[c.lower()] = 1 + counts.get(c.lower(), 0)
    return counts

def pretty_print_character_counts(counts):
    for c, ct in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f'{c}: {ct}')




