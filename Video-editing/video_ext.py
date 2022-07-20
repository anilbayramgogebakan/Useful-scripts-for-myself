#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:21:19 2022

@author: anilbayramg
"""
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

START = 0
FINISH = 18
INDEX = 1
NAME = "foggy4"

# ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
ffmpeg_extract_subclip(NAME+".avi", START, FINISH, targetname=(NAME+"-"+str(INDEX)+".avi"))
ffmpeg_extract_subclip(NAME+".mp4", START, FINISH, targetname=(NAME+"-"+str(INDEX)+".mp4"))

# ffmpeg_extract_subclip("foggy12-out.mp4", 62, 76, targetname="final2.mp4")