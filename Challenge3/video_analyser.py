# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:10:20 2017

@author: tadah
"""
import os
import cv2
from scipy import signal
import numpy as np

def keyframe():
    for filename in os.listdir('.\subsubvideos'):
        #print filename
        vidcap = cv2.VideoCapture('.\\subsubvideos\\' + filename)
        success,image = vidcap.read()
        count = 0
        result = []
        success = True
        while success:
            success,image = vidcap.read()
            if success:
                if (count == 0):
                    keyframe = image
                else:
                    result = count_true(LSH(keyframe,image))
                count += 1
            #if (count == 12):
            #    break;
        vidcap.release()
        #print count

def hash(differences):
   hexi = []
   for difference in differences:
       decimal_value = 0
       hex_string = []
       for index, value in enumerate(difference):
           if value:
               decimal_value += 2**(index % 8)
           if (index % 8) == 7:
               hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
               decimal_value = 0
       ''.join(hex_string),
       hexi.append(hex_string[0])
   return hexi

def LSH(image1, image2):
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    pix_image1 = cv2.resize(gray_image1, (8,9))
    pix_image2 = cv2.resize(gray_image2, (8,9))
    lsh = [i > j for i,j in zip(pix_image1,pix_image2)]
    return lsh

def count_true(differences):
   hexi = 0
   for difference in differences:
       decimal_value = 0
       hex_string = 0
       for index, value in enumerate(difference):
           if value == True:
               hexi +=1       
   return hexi

keyframe()