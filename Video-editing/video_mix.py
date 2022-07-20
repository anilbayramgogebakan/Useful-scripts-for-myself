#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:29:46 2022

@author: anilbayramg
"""
from moviepy.editor import VideoFileClip, concatenate_videoclips, clips_array

INDEX = 1
NAME = "foggy4"

clip1 = VideoFileClip(NAME+"-"+str(INDEX)+".mp4")
clip2 = VideoFileClip(NAME+"-"+str(INDEX)+".avi")

final_clip = clips_array([[clip1, clip2]])

# final_clip.resize(width=480).write_videofile("my_stack.mp4")

final_clip.write_videofile(NAME+"-"+str(INDEX)+"-out.mp4")