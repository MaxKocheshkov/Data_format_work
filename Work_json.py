import json
from collections import Counter

with open("files/newsafr.json", encoding='utf-8') as datafile:
    json_data = json.load(datafile)

for headers in json_data.values():
  channel = headers['channel']
  for item in channel.values():
    if type(item) == list:
      for dct_news in item:
        description = dct_news.get('description')
        description = description.lower().split()


output_value = Counter(description)
print(f'Наиболее часто встречающиеся слова : {output_value.most_common(10)}')