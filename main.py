import json
import xml.etree.ElementTree as ET
import count_words as c_w

def work_json():
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

def work_xml():
    parser = ET.XMLParser(encoding="utf-8")

    tree = ET.parse("files/newsafr.xml", parser)
    titles = []
    root = tree.getroot()
    xml_title = root.find("channel/title")
    xml_items = root.findall("channel/item")
    for xmli in xml_items:
        xml_descripction = xmli.findall("description")
        for words in xml_descripction:
            words = words.text
            find_words = words.lower()
            tmp_file = open("temp.txt", "a", encoding = 'utf-8')
            tmp_file.write(find_words)
            tmp_file.close()

    output_message = c_w.count_words()
    print(output_message)

def main():
  while True:
    print('Введите команду для работы с файлом (j - json, x - xml, q - выход): ')
    user_input = input()
    if user_input == 'j':
      work_json()
    elif user_input == 'x':
      work_xml()
    elif user_input == 'q':
      print('До свидания!')
      break

main()