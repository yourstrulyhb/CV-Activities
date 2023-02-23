# CMSC 174 LAB. 1.3 Chessboard
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



""" Change color of alternating 100x100 blocks (of pixels) 
    Changes rows 0-99, columns 0-99 into white, rows 0-99 columns 200-299 into white, and so on."""

row_start=0 # Start from row 0-99 
while row_start < sq_img_dim:
    
    if row_start%200 == 0:
        col_start=0   
    else:
        col_start=100
        
    while col_start < sq_img_dim:
        mat[row_start:row_start+99, col_start:col_start+99] = [255, 255, 255]
        col_start+=200
        
    row_start+=100
   

""" Display 800x800 image """
cv2.imshow("image", mat)
cv2.waitKey(0)
