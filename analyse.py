# coding: utf-8

from janome.tokenizer import Tokenizer
import re
import unicodedata
import string


def morphological(text):
    t = Tokenizer()
    token = t.tokenize(text)
    words = []
    for n in token:
        word = n.surface
        word = re.sub(r'[!-~]', "", word)  # 半角記号,数字,英字
        word = re.sub(r'[︰-＠]', "", word)  # 全角記号
        word = re.sub('\n', " ", word)  # 改行文字
        word = re.sub('。', " ", word)
        word = re.sub('、', " ", word)
        word = re.sub('・', " ", word)
        word = re.sub(' ', " ", word)
        word = re.sub('　', " ", word)

        if len(word) > 1 and n.part_of_speech.find('名詞') > -1:
            words.append(word)
    return list(set(words))
