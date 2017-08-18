# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 16:03:44 2017

@author: hexo
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                'key2' : ['one', 'two', 'one', 'two', 'one'],
                'data1' : np.random.randint(0,10,5),
                'data2' : np.random.randint(0,10,5)})