import re
import os
from collections import Counter

def count_words():
    with open("temp.txt", 'r', encoding = 'utf-8') as f:
        word_dict = f.read()
        word_dict = word_dict.lower()
        output_words = re.findall(r"\b[а-я]{6,}", word_dict)

    c = Counter(output_words)
    print(f'Наиболее часто встречающиеся слова : {c.most_common(10)}')

    file_tmp = 'temp.txt'
    os.remove(file_tmp)