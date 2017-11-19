# -*- coding: utf-8 -*-
from selenium import webdriver
import time


def start(words):
    for word in words:
        url = 'http://www.google.co.jp/'
        browser = webdriver.Firefox()
        browser.get(url)
        el = browser.find_element_by_css_selector("#lst-ib")
        el.send_keys(word)
        browser.find_element_by_css_selector(".jsb > center:nth-child(1) > input:nth-child(1)").click()
        time.sleep(0.1)
