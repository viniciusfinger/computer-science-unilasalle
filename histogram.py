import re

file = open("casmurro.txt", 'r')

def clean_word(word):
    return re.sub(r'[^\w\s]', '', word).lower()

def order_dict(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

words_count = {}

for line in file:
    for word in line.split():
        word = clean_word(word)
        words_count[word] = words_count.get(word, 0) + 1

words_count = order_dict(words_count)

for word, count in words_count.items():
    print(f"{word}: {count}")