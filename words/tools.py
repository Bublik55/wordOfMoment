import pymorphy2
import re
morph = pymorphy2.MorphAnalyzer()
def to_normal_form(str):
    return morph.parse(str)[0].lexeme[0].word.capitalize()