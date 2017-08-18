# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 16:03:44 2017

@author: hexo
"""

import pandas as pd
import numpy as np


data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4,
                  'k2': [1, 1, 2, 3, 3, 4, 4]})
data

data.duplicated()

data.drop_duplicates()

data['v1'] = range(7)
data.drop_duplicates(['k1'])

data.drop_duplicates(['k1', 'k2'], take_last=True)




#重复数据
data = pd.Series([1., -999., 2., -999., -1000., 3.])
data

data.replace(-999, np.nan)

data.replace([-999, -1000], np.nan)

data.replace([-999, -1000], [np.nan, 0])

data.replace({-999: np.nan, -1000: 0})

