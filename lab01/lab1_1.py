# CMSC 174 LAB. 1.1 Horizontal stripes
# Hannah Bella C. Arceño
# FEB. 2023

import numpy as np
import cv2
  
sq_img_dim=800

""" Initialize 800x800x3 matrix of black pixels.
    800x800 => dimension of image
    3: length of pixel array """
mat = np.full((sq_img_dim, sq_img_dim, 3), 0, dtype = np.uint8) # Pixel array = [0,0,0]; represents black pixel
# Black so that it is relatively faster to initialize 


""" Changes row color of rows:
    0-99, 200-299, 400-499, and 600-699
    to white. """
white_start = 0
while white_start < sq_img_dim:
    mat[white_start : white_start+99] = [255, 255, 255] # Change row color to white
    white_start += 200

    
""" Display 800x800 image """
cv2.imshow("image", mat)
cv2.waitKey(0)