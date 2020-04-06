# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:24:27 2020

@author: vinnr
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def matplotlib_display(BGR_img, title, position):
    
   
    RGB_img = BGR_img[:,:,::-1] #convert to RGB for matplotlib case
   
    disp = plt.subplot(3, 3, position)
    plt.imshow(RGB_img)
    plt.title(title)
    plt.axis('off')

# set title and create the dimensions of figure 
    
plt.figure(figsize=(12,6))
plt.suptitle("Bitwise operations", fontsize=14)

# create an image
img_1 = np.zeros((300,300), dtype="uint8")
cv2.rectangle(img_1, (10,10), (110,110), (255,255,255), -1)
cv2.circle(img_1, (200,200), 50, (255,255,255), -1)

# second image
img_2 = np.zeros((300,300), dtype="uint8")
cv2.rectangle(img_1, (50,50), (150,150), (255,255,255), -1)
cv2.circle(img_1, (225,200), 50, (255,255,255), -1)


# Bitwise OR
bitwise_or = cv2.bitwise_or(img_1, img_2)

# Bitwise AND
bitwise_and = cv2.bitwise_and(img_1, img_2)

# Bitwise XOR
bitwise_xor = cv2.bitwise_xor(img_1, img_2)

# Bitwise NOT
bitwise_not_1 = cv2.bitwise_not(img_1)

# Bitwise NOT
bitwise_not_2 = cv2.bitwise_not(img_2)

# show with matplot lib
matplotlib_display(cv2.cvtColor(img_1, cv2.COLOR_GRAY2BGR), "image 1", 1)
matplotlib_display(cv2.cvtColor(img_2, cv2.COLOR_GRAY2BGR), "image 2", 2)
matplotlib_display(cv2.cvtColor(bitwise_or, cv2.COLOR_GRAY2BGR), "image 1 OR image 2", 3)
matplotlib_display(cv2.cvtColor(bitwise_and, cv2.COLOR_GRAY2BGR), "image 1 AND image 2", 4)
matplotlib_display(cv2.cvtColor(bitwise_xor, cv2.COLOR_GRAY2BGR), "image 1 XOR image 2", 5)
matplotlib_display(cv2.cvtColor(bitwise_not_1, cv2.COLOR_GRAY2BGR), "NOT (image 1)", 6)
matplotlib_display(cv2.cvtColor(bitwise_not_2, cv2.COLOR_GRAY2BGR), "NOT (image 2)", 7)
    
# showing with operations with images

image = cv2.imread("tom_cruise.jpg") # size of image = 672 * 378

# create a blank image of the same size
img_3 = np.zeros((672,378), dtype ="uint8")
cv2.circle(img_1, (150,150), 150, (255,255,255), -1)

# perform bitwise operation
bitwise_ex = cv2.bitwise_and(image, image, mask = img_3)

# display these two images

matplotlib_display(cv2.cvtColor(img_3, cv2.COLOR_GRAY2BGR), "Image 3", 8)
matplotlib_display(bitwise_ex, "Image loaded on another", 9)

# display figure
plt.show()
   