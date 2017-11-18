# coding: utf-8

from google_search import GoogleSearch
from screenshot import shot_cursor
from ocr import ocr_read
from analyse import morphological

shot_cursor()
words = morphological(ocr_read())

gs = GoogleSearch(1)

# gs.search(words[0])
# gs.search_list(words)
gs.search('ウェアラブル')
# gs.search('AI')
# gs.search('Python')
gs.view()

