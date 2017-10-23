# coding: utf-8
from pyquery import PyQuery as pq
import requests

page_num = 110  # 100件までが限界
query = '機械学習'
query_url = 'http://www.google.co.jp/search?hl=jp&num=' + str(page_num) + '&q=' + query
headers = {'User-Agent': 'Mozilla/5.0'}
articles = []

response = requests.get(query_url, headers=headers)
dom = pq(response.text)

for elem in dom.find('div > h3 > a'):
    text = pq(elem).text()
    s_url = pq(elem).attr('href')
    articles.append([text, s_url.lstrip('/url?q=')])

[print(x[0], ':', x[1]) for x in articles]

print('記事は全部で', len(articles), '件')
