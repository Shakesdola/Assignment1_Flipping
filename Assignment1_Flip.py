#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
from PIL import Image
import numpy as np

im = Image.open("number.png")
im.show()

#To store the image in a Numpy array
im_array = np.array(im)

#Modify the order of the array to get a new image flipping vertically
im_up = im_array[::-1]
im2 = Image.fromarray(im_up)
im2.show()

#Modify the order of the array to get a new image flipping horizontally
im_lr = im_array[:,::-1]
im3 = Image.fromarray(im_lr)
im3.show()


# In[ ]:




