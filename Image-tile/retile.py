#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:52:26 2022

@author: anilbayramg
"""

import cv2
import os 
import numpy as np


def col_and_row(image_name):
        # 'save_1_0.jpg' is the example format
    col_num = int(image_name.split("_")[1])
    row_num = image_name.split("_")[2]
    row_num = int(row_num.split(".")[0])
    return col_num, row_num


if not os.path.exists("./dene"):
    raise Exception("Tiled images cannot found!") 
    
parent_dir = os.getcwd()
    

im_arr = sorted(os.listdir("./dene"))
result_path = os.path.join(parent_dir, "dene")
last_im_path = os.path.join(result_path, im_arr[-1])
last_im = cv2.imread(last_im_path)

im_height = last_im.shape[0]
im_width = last_im.shape[1]

col_num, row_num = col_and_row(im_arr[-1])


#col_num = int(im_arr[-1].split("_")[1])
#row_num = im_arr[-1].split("_")[2]
#row_num = int(row_num.split(".")[0])

final_im = np.zeros(((row_num+1)*im_height,(col_num+1)*im_width, 3))


for im_part in im_arr:
    im_path = os.path.join(result_path, im_part)
    tiled = cv2.imread(im_path)
    
    col, row = col_and_row(im_part)
    
    final_im[im_height*row:im_height*(row+1), im_width*col:im_width*(col+1)] = tiled
    
        
cv2.imwrite("final_im_6.jpg", final_im)
    

