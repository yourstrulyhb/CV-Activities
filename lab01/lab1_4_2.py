# CMSC 174 LAB. 1.4 Different Colors
# Hannah Bella C. Arceño
# FEB. 2023

import numpy as np
import cv2
import random

def rand_color_num():
    c = random.randrange(256)
    return c

sq_img_dim=800

""" Initialize 800x800x3 matrix of black pixels.
    800x800 => dimension of image
    3: length of pixel array """
mat = np.full((sq_img_dim, sq_img_dim, 3), 0, dtype = np.uint8) # Pixel array = [0,0,0]; represents black pixel
# Black so that it is relatively faster to initialize 


""" Changes column color of columns """
white_start = 0
while white_start < sq_img_dim:
    mat[0:800, white_start : white_start+99] = [255, rand_color_num(), rand_color_num()] 
    # <select all rows> , <selected columns, 100 width>
    white_start += 100

    
""" Display 800x800 image """
cv2.imshow("image", mat)
cv2.waitKey(0)
