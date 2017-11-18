# coding: utf-8

from janome.tokenizer import Tokenizer


def morphological(text):
    t = Tokenizer()
    token = t.tokenize(text)
    words = []
    for n in token:
        print(n.surface)
        words.append(n.surface)
    return words
