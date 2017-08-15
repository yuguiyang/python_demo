# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 15:45:36 2017

@author: hexo
"""

import pandas as pd

import numpy as np

a = pd.Series([np.nan,2.5,np.nan,3.5,4.5,np.nan]
                    ,index=['f','e','d','c','b','a'])

b = pd.Series(np.arange(len(a),dtype=np.float64)
                    ,index=['f','e','d','c','b','a'])

b[-1] = np.nan

print(a)
print(b)