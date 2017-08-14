# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:01:31 2017

@author: hexo
"""

import numpy as np
import matplotlib.pyplot as plt

#配置每次生成的随机数相同
np.random.seed(0)

mu = 200
sigma = 25
x = np.random.normal(mu, sigma, size=500)

print(x)

ax0 = plt.gca()

ax0.hist(x, 20, normed=1, histtype='stepfilled', facecolor='g', alpha=0.75)
ax0.set_title('stepfilled')

plt.show()