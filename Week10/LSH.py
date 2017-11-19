from PIL import Image
import numpy as np


def LSH(image1, image2):
    pix_image1 = image1.resize((8,9),Image.ANTIALIAS)
    pix_image2 = image2.resize((8,9),Image.ANTIALIAS)
    
    list_image1 = list(pix_image1.getdata())
    list_image2 = list(pix_image2.getdata())
    
    lsh = [i > j for i,j in zip(list_image1,list_image2)]
    
    return lsh

cat_one = Image.open('Cat1.png').convert('LA')
cat_two = Image.open('Cat2.png').convert('LA')

print LSH(cat_one,cat_two)

dog_one = Image.open('dog1.jpg').convert('LA')
print LSH(cat_one,dog_one)