import json
import count_words as c_w

with open("files/newsafr.json", encoding='utf-8') as datafile:
    json_data = json.load(datafile)

for headers in json_data.values():
  channel = headers['channel']
  for item in channel.values():
    if type(item) == list:
      for dct_news in item:
        description = dct_news.get('description')
        description = description.lower()
        temp_file = open("temp.txt", "a", encoding = 'utf-8')
        temp_file.write(description)
        temp_file.close()

output_message = c_w.count_words()
print(output_message)