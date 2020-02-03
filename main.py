import json
import xml.etree.ElementTree as ET


def repetition_selection(list_words,quantity_words,length_words):
    description_str = " ".join(list_words)
    words = description_str.split(" ")

    long_words_list = []

    for word in words:
        word = word.lower()
        if len(word) > length_words:
            long_words_list.append(word)

    def get_count(symbol):
        x = long_words_list.count(symbol)
        return x

    sorted_list = (sorted(long_words_list, key=get_count, reverse=True))

    unique_list = []
    for word in sorted_list:
        if word not in unique_list:
            unique_list.append(word)

    return unique_list[0:quantity_words]


#задача 1
with open("newsafr.json", encoding='utf-8') as f:
    whole_file = json.load(f)

items = whole_file["rss"]["channel"]["items"]

description_list = []
for news in items:
    description = news["description"]
    description_list.append(description)

print("10 самых часто встречающихся слов длиннее 6 символов из json: ", repetition_selection(description_list, 10, 6))


#задача 2
tree = ET.parse("newsafr.xml")
root = tree.getroot()
descriptions = root.findall("channel/item/description")

description_list = []
for description in descriptions:
    description_list.append(description.text)

print("10 самых часто встречающихся слов длиннее 6 символов из xml: ", repetition_selection(description_list, 10, 6))