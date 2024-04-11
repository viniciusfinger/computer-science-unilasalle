import re

file_name = "casmurro.txt"
file = open(file_name, 'r')

def clean_word(word):
    return re.sub(r'[^\w\s]', '', word).lower()

def order_dict(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))

def print_dict(dictionary):
    for word, count in dictionary.items():
        print(f"{word}: {count}")

words_count = {}

for line in file:
    for word in line.split():
        word = clean_word(word)
        words_count[word] = words_count.get(word, 0) + 1

words_count = order_dict(words_count)

print_dict(words_count)