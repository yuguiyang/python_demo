# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:19:08 2017

@author: yuguiyang
"""

import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 
  

fig,axes = plt.subplots()  
    
ims= []
for i in range(5):
    ims.append(axes.plot(np.random.rand(10)))

im_ani = animation.ArtistAnimation(fig, ims, interval=500, repeat_delay=3000,
                                   blit=True)
print(ims)
plt.show() 