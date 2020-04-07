import xml.etree.ElementTree as ET
from collections import Counter

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
        find_words = words.lower().split()

output_value_xml = Counter(find_words)
print(f'Наиболее часто встречающиеся слова : {output_value_xml.most_common(10)}')

