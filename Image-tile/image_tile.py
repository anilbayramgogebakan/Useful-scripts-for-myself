#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:52:48 2022

@author: anilbayramg
"""

import cv2
import os 

if not os.path.exists("./tile_results"):
    os.mkdir("./tile_results")

im =  cv2.imread("/home/anilbayramg/Desktop/Github-desktop/Cycle-Dehaze/my_images/example-images/foggyHouse.jpg")
#im = cv2.resize(im,(1000,500))
out_size_x = 1024
out_size_y = 768

imgheight=im.shape[0]
imgwidth=im.shape[1]


M = imgheight//out_size_y
N = imgwidth//out_size_x


for y in range(0, M):
    for x in range(0, N):
        
        tiles = im[y*out_size_y:(y+1)*out_size_y, x*out_size_x:(x+1)*out_size_x]

        cv2.imwrite("./tile_results/save_" + str(x) + '_' + str(y)+".jpg",tiles)
