# coding: utf-8
import webbrowser
from time import sleep


def search(word):
    url = 'https://ja.wikipedia.org/wiki/' + word
    webbrowser.open(url)


def search_list(words):
    for word in words:
        url = 'https://ja.wikipedia.org/wiki/' + word
        webbrowser.open(url)
        sleep(0.5)



