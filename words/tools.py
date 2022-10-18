import pymorphy2
import re
morph = pymorphy2.MorphAnalyzer()
def to_normal_form(str):
    # print(morph.parse(str)[0].lexeme[0].word)
    return morph.parse(str)[0].lexeme[0].word.capitalize()