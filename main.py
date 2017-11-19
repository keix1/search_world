# coding: utf-8

from google_search import GoogleSearch
from screenshot import shot_cursor
from ocr import ocr_read
from analyse import morphological
import wikipedia_search
import time
import browser

while True:
    shot_cursor()
    words = morphological(ocr_read())
    print(words)
    # wikipedia_search.search_list(words)
    browser.start(words)
    time.sleep(5)

# gs = GoogleSearch(1)

# gs.search(words[0])
# gs.search_list(words)
# gs.search('ウェアラブル')
# gs.search('AI')
# gs.search('Python')
# gs.view()

