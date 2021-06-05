#!/usr/bin/env python
# coding: utf-8

# In[2]:


#first we import all necessary libraries i.e numpy pandas , cv2 for computer vision


import numpy as np
import cv2
import pandas as pd


# In[3]:


# here we have taken one colored image of actor using cv2




#color image 
photo=cv2.imread("shah.jpg")
cv2.imshow('SRK',photo)
#cv2.imshow("crop",photo)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:






#here we used rectangle to show the croped area


gunjna=cv2.rectangle(photo,(250,120),(400,270), (255, 0, 0),2)
#cv2.imshow('link',gunjna)


cv2.imshow("gunjna",gunjna)
cv2.waitKey(0)
cv2.destroyAllWindows()



# In[4]:


#here we cropped the image and stored into the p1 variable

p1=photo[120:270,250:400]
#cropped_color=np.expand_dims(photo,axis=2)



# for image showing 


cv2.imshow("croped image",p1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


# balck and white image 

photo=cv2.imread("shah.jpg")

#converted color image to black and white 


grey_image=cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
#cv2.imshow('srk_b',grey_image)


cv2.imshow('croped',grey_image)


cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:





#cropped the image


p2=grey_image[120:270,250:400]
g2=p2


#as the black and white image is 2d i have converted it to the 3d
p2=np.expand_dims(grey_image,axis=2)
p2.shape
cv2.imshow('croped',p2)


cv2.waitKey(0)
cv2.destroyAllWindows()


# In[7]:


#here we swaapped the grey cropped image to the colored photo


photo[120:270,250:400]=p2[120:270,250:400]


#final output


cv2.imshow("final-output",photo)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[8]:


# now we are going to add two images side by side 

photo1=cv2.imread('srk2.jpg')
cv2.imshow("srk",photo1)
cv2.waitKey(0)
cv2.destroyAllWindows()






# In[9]:


new=np.hstack([photo,photo1])


# In[10]:


cv2.imshow("srk",new)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




