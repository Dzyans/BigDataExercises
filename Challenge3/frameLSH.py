# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:01:12 2017

@author: s123725
"""

import cv2
from moviepy.editor import VideoFileClip

clip = VideoFileClip('.videos\00SXM76KD1X2.mp4')
count =1
for frames in clip.iter_frames():
    gray_frames = cv2.cvtColor(frames, cv2.COLOR_RGB2GRAY)
    print frames.shape
    print gray_frames.shape
    count+=1
print count