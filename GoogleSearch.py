# coding: utf-8
from pyquery import PyQuery as pq
import requests

class GoogleSearch:
    def __init__(self, page_num=100):
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.articles = []
        self.all_query = []
        self.all_query_url = []

        self.page_num = page_num
        self.query = 'keyword'
        self.query_url = 'http://www.google.co.jp/search?hl=jp&num=' + str(self.page_num) + '&q=' + self.query

    def search(self, query='keyword'):
        self.query_url = 'http://www.google.co.jp/search?hl=jp&num=' + str(self.page_num) + '&q=' + self.query
        self.query = query
        self.all_query.append(self.query)
        self.all_query_url.append(self.query_url)

        response = requests.get(self.query_url, headers=self.headers)
        dom = pq(response.text)

        for elem in dom.find('div > h3 > a'):
            text = pq(elem).text()
            s_url = pq(elem).attr('href')
            self.articles.append([text, s_url.lstrip('/url?q=')])

    def view(self):
        [print(x[0], ':', x[1]) for x in self.articles]
        print()
        print('見つけた記事は全部で', len(self.articles), '件')
        print()
        print('検索キーワードは', len(self.all_query), '件')
        [print('「', x, '」', end='') for x in self.all_query]

if __name__ == '__main__':
    gs = GoogleSearch()
    gs.search('機械学習')
    gs.search('AI')
    gs.view()
