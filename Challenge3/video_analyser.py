# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:10:20 2017

@author: tadah
"""
import os
import cv2
from PIL import Image
import numpy as np


def keyframe():
    for filename in os.listdir('.\subvideos'):
        #print filename
        vidcap = cv2.VideoCapture('.\\subsubvideos\\' + filename)
        success,image = vidcap.read()
        count = 0
        success = True
        while success:
            success,image = vidcap.read()
            if success:
                if (count == 0):
                    keyframe = image
                else:
                    result = count_true(LSH(keyframe,image))
                    print result
                        count += 1
            if (count == 2):
                break;
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
    
    pix_image1 = pixelize(gray_image1)
    pix_image2 = cv2.resize(gray_image2, (8,9))
    
    cv2.imshow('lal',pix_image1)
    cv2.imshow('asd',pix_image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    lsh = [i > j for i,j in zip(pix_image1,pix_image2)]
    return lsh

def pixelize(image):
    backgroundColor = (0,)*3
    pixelSize = 9
    
    image = image.resize((image.size[0]/pixelSize, image.size[1]/pixelSize), Image.NEAREST)
    image = image.resize((image.size[0]*pixelSize, image.size[1]*pixelSize), Image.NEAREST)
    pixel = image.load()
    
    for i in range(0,image.size[0],pixelSize):
      for j in range(0,image.size[1],pixelSize):
        for r in range(pixelSize):
          pixel[i+r,j] = backgroundColor
          pixel[i,j+r] = backgroundColor
    
    return image

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