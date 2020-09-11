#!/usr/bin/env python
# coding: utf-8

# In[1]:


import face_recognition


# In[2]:


import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import os


# In[4]:


import pandas as pd
test_set = pd.read_csv("test.csv")


# In[5]:


test_set.head()


# In[6]:


"""
Appending all the images name in test_images list
"""
test_images=[]
for img in list(test_set["Name"]):
    test_images.append(img)


# In[7]:


print(len((test_images)))


# In[ ]:


"""
Using face_recognition to detect faces from the images
"""
from PIL import Image
head_count=[]
test_imgs=[]
for img in test_images[0:1]:
    test_imgs.append(img)
    bbox=[]
    image = os.path.join("image_data",img)
    #imge = cv2.imread(image)
    #cv2.imshow("image",imge)
    image = face_recognition.load_image_file(image)
    
    face_locations = face_recognition.face_locations(image)

    for face_location in face_locations:
        #print(face)
        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        bbox.append((top, right, bottom, left))
        #pil_image = Image.fromarray(face_image)
        #pil_image.show()

    head_count.append(len(bbox))

cv2.waitKey(0)
cv2.destroyAllWindows()

