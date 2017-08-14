# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 16:24:02 2017

@author: hexo
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties  

#引用Windows中的字体
font_set = FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc', size=15)

plt.figure(u'中文')

plt.plot([1,2,3,4],[-2,-1,0,1])

plt.title(u'今天',fontproperties=font_set)

plt.xlabel(u'明天',fontproperties=font_set)

plt.ylabel(u'昨天',fontproperties=font_set)

plt.show()