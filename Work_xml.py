import xml.etree.ElementTree as ET
import count_words as c_w

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
        temp_file = open("temp.txt", "a", encoding = 'utf-8')
        temp_file.write(find_words)
        temp_file.close()

output_message = c_w.count_words()
print(output_message)

