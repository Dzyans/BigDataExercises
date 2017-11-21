# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:10:20 2017

@author: tadah
"""

import cv2
vidcap = cv2.VideoCapture('C:/Users/tadah/Documents/BigDataExercises/Challenge3/videos/0A93T546KVUM.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  #print('Read a new frame: ', success)
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1 

print(count)