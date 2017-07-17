import chardet
import json
import re
from collections import Counter


def get_file():
    file = input()
    with open(file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = result['encoding']
    json_file = open(file, encoding=s)
    json_news = json.load(json_file)
    return json_news


def get_top_10():
    pattern = r'\b[a-zA-Zа-яА-Я]{1}[a-zA-Zа-яА-Я\-]{5,}[a-zA-Zа-яА-Я]{1}\b'
    news = get_file()['rss']['channel']['items']
    words = []
    for news_item in news:
        news_words = news_item['description']
        suitable_words = re.findall(pattern, news_words)
        words = words + suitable_words
    words_count = Counter(words)
    top10 = words_count.most_common(10)
    for item in top10:
        print(item[0] + ', ' + '%d раз(а)' % (item[1]))

get_top_10()