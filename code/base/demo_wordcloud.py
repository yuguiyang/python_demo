 # -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 23:07:42 2017

@author: yuguiyang
"""

from os import path
from wordcloud import WordCloud
import jieba

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'hello.txt'),encoding='utf-8').read()

text_cut = jieba.cut(text , cut_all=False)
font = r'C:\Windows\Fonts\simsun.ttc'
# Generate a word cloud image
wordcloud = WordCloud(font_path=font).generate(' '.join(text_cut))

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

